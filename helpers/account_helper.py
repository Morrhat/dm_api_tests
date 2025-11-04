import time
from json import loads

from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi


def retrier(
        function
        ):
    def wrapper(
            *args,
            **kwargs
            ):
        token = None
        count = 0
        while token is None:
            print(f"Попытка получения токена номер {count}")
            token = function(*args, **kwargs)
            count += 1
            if count == 5:
                raise AssertionError("Превышено количество попыток получения активационного токена")
            if token:
                return token
            time.sleep(1)

    return wrapper


class AccountHelper:
    def __init__(
            self,
            dm_account_api: DMApiAccount,
            mailhog: MailHogApi
    ):
        self.dm_account_api = dm_account_api
        self.mailhog = mailhog

    # Авторизованный клиент
    def auth_client(self, login: str, password: str):
        response = self.user_login(login=login, password=password)
        token: dict[str, str] = {'x-dm-auth-token': response.headers['x-dm-auth-token']}
        self.dm_account_api.account_api.set_headers(token)
        self.dm_account_api.login_api.set_headers(token)


    # Регистрация и активация нового пользователя

    def register_new_user(
            self,
            login: str,
            password: str,
            email: str
           ):
        json_data = {
            'login': login,
            'email': email,
            'password': password,
        }

        # Регистрация пользователя

        response = self.dm_account_api.account_api.post_v1_account(json_data=json_data)
        assert response.status_code == 201, f"Пользователь не был создан {response.json()}"
        # Активация
        token = self.get_activation_token(login=login)
        response = self.dm_account_api.account_api.put_v1_account_token(token=token)
        assert response.status_code == 200, f"Пользователь не был активирован {response.json()}"
        return response

    # Авторизация

    def user_login(
            self,
            login: str,
            password: str,
            remember_me: bool = True
            ):
        json_data = {
            'login': login,
            'password': password,
            'rememberMe': remember_me,
        }

        response = self.dm_account_api.login_api.post_v1_account_login(json_data=json_data)
        # assert response.status_code == 200, f"Пользователь не смог авторизоваться {response.json()}"
        return response

    # Смена email

    def change_email(
            self,
            login: str,
            password: str,
            email: str
            ):
        json_data = {
            'login': login,
            'password': password,
            'email': email,
        }
        response = self.dm_account_api.account_api.put_v1_account_email(json_data=json_data)
        assert response.status_code == 200, f"Email пользователя не поменялся {response.json()}"
        return response

    # Получение токена из письма
    @retrier
    def get_activation_token(
            self,
            login: str
    ):
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        assert response.status_code == 200, f"Письма не были получены {response.json()}"

        # Получение токена
        token = None
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            user_login = user_data['Login']
            if user_login == login:
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
        assert token is not None, f"Токен для пользоваетля {login} не был получен"
        return token


    # Инициализация сброса пароля
    def change_password(
            self,
            login: str,
            email: str,
            password: str
            ):
        json_data = {
            'login': login,
            'email': email,
        }
        response = self.dm_account_api.account_api.post_v1_account_password(json_data=json_data)
        assert response.status_code == 200, f"Сброс пароля не инициализирован {response.json()}"


    # Смена пароля с пробросом авторизационного токена в хэдэры
    #     и указанием токена для сброса пароля из письма
    def get_password_token(
            self,
            login: str,
            password: str,
            token: str = None
            ):
        # Получение писем
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        assert response.status_code == 200, f"Письма не были получены {response.json()}"

        # Получение токена
        token = None
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            if 'ConfirmationLinkUri' not in user_data:
                continue
            user_login = user_data['Login']
            print(user_login)
            print(user_data)
            if user_login == login:
                token = user_data['ConfirmationLinkUri'].split('/')[-1]
                break
        assert token is not None, f"Токен сброса пароля {login} не был получен"

        # Активация токена сброса
        json_data = {
            "login": login,
            "token": token,
            "oldPassword": password,
            "newPassword": "987654321"
        }
        response = self.dm_account_api.account_api.put_v1_account_password(json_data=json_data)
        assert response.status_code == 200, f"Пароль не был изменён {response.json()}"
        return response


