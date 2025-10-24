from json import loads

from dm_api_account.apis.account_api import AccountAPI
from dm_api_account.apis.login_api import LoginAPI
from api_mailhog.apis.mailhog_api import MailhogAPI


def test_put_v1_account_email():
    # Регистрация пользователя

    account_api = AccountAPI(host='http://5.63.153.31:5051')
    login_api = LoginAPI(host='http://5.63.153.31:5051')
    mailhog_api = MailhogAPI(host='http://5.63.153.31:5025')

    login = 'kristinochka_test43'
    password = '123456789'
    email = f'{login}@mail.com'
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f"Пользователь не был создан {response.json()}"

    # Получить письма из почтового сервера

    response = mailhog_api.get_api_v2_messages()
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Письма не были получены {response.json()}"
    #  pprint.pprint(response.json())

    # Получить активационный токен

    token = get_activation_token_by_login(login, response)
    assert token is not None, f"Токен для пользоваетля {login} не был получен"

    # Активация пользователя

    response = account_api.put_v1_account_token(token=token)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Пользователь не был активирован {response.json()}"

    # Авторизоваться

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Пользователь не смог авторизоваться {response.json()}"

    # Смена email

    json_data = {
        'login': login,
        'password': password,
        'email': email,
    }
    response = account_api.put_v1_account_email(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Email пользователь не поменялся {response.json()}"

    # Авторизация под старыми данными неудачная

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 403, f"Пользователь смог авторизоваться под старыми данными {response.json()}"

    # Получить письма из почтового сервера по новому email для подтверждения смены email

    response = mailhog_api.get_api_v2_messages()
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Письма не были получены {response.json()}"
    #  pprint.pprint(response.json())

    # Получить активационный токен

    token = get_activation_token_by_login(login, response)
    assert token is not None, f"Токен для пользоваетля {login} не был получен"

    # Активация нового токена

    response = account_api.put_v1_account_token(token=token)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Пользователь не был активирован {response.json()}"

    # Авторизоваться

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Пользователь авторизовался {response.json()}"


def get_activation_token_by_login(
        login,
        response
):
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body'])
        user_login = user_data['Login']

        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
    return token
