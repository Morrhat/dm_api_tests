from json import loads

from dm_api_account.apis.account_api import AccountAPI
from dm_api_account.apis.login_api import LoginAPI
from api_mailhog.apis.mailhog_api import MailhogAPI


def test_post_v1_account():
    # Регистрация пользователя

    account_api = AccountAPI(host='http://5.63.153.31:5051')
    login_api = LoginAPI(host='http://5.63.153.31:5051')
    mailhog_api = MailhogAPI(host='http://5.63.153.31:5025')

    login = 'kristinochka_test40'
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
