
def attempt(n=5):

    def decorator(func):
        def wraps(*args, **kwargs):
            print("******************")
            print(n)
            func(*args, **kwargs)
            print("******************")
            return
        return wraps
    return decorator


@attempt(n=5)
def my_print(name):
    print(f"Hello everybody {name}")
@attempt(n=5)
def my_print1():
    print("Hello every")
@attempt(n=5)
def my_print2(name):
    print(f"Hello body {name}")
@attempt(n=5)
def my_print3(name):
    print(f"Hello qitti {name}")
@attempt(n=5)
def my_print4(name):
    print("Hello ebony")

my_print(name = 'Kamadzi')
my_print1()
my_print2(name = 'Faseless')
my_print3(name = 'Tikiro')
my_print4(name = 'Kamadzi')


def get_activation_token(
        self,
        login: str
):
    # Получение писем
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
    # Активация пользователя
    token = self.get_activation_token(login=login)
    response = self.dm_account_api.account_api.put_v1_account_token(token=token)
    assert response.status_code == 200, f"Пользователь не был активирован {response.json()}"
    return response














