from json import loads

from helpers.account_helper import AccountHelper
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi
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

def test_put_v1_account_token():
    # Регистрация пользователя

    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)

    account = DMApiAccount(configuration=dm_api_configuration)
    mailhog = MailHogApi(configuration=mailhog_configuration)

    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog)

    login = 'kristinochka_test146'
    password = '123456789'
    email = f'{login}@mail.com'
    account_helper.register_new_user(login=login, password=password, email=email)

    # Получить письма из почтового сервера

    response = mailhog.mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, f"Письма не были получены {response.json()}"
    #  pprint.pprint(response.json())

    # Получить активационный токен из письма и активировать

    account_helper.get_token_by_email(login=login)
