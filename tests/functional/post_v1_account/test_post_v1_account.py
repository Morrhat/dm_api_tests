from json import loads

from dm_api_account.apis.account_api import AccountAPI
from dm_api_account.apis.login_api import LoginAPI
from api_mailhog.apis.mailhog_api import MailhogAPI
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
            #sort_keys=True

        )
    ]
)


def test_post_v1_account():
    # Регистрация пользователя
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)

    account_api = AccountAPI(configuration=dm_api_configuration)
    login_api = LoginAPI(configuration=dm_api_configuration)
    mailhog_api = MailhogAPI(configuration=mailhog_configuration)

    login = 'kristinochka_test127'
    password = '123456789'
    email = f'{login}@mail.com'
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data=json_data)
    assert response.status_code == 201, f"Пользователь не был создан {response.json()}"
