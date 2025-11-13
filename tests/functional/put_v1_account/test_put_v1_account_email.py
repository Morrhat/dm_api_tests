import allure

from checkers.http_checkers import check_status_code_http
from checkers.put_v1_account_email import PutV1AccountEmail


@allure.suite('Тесты на проверку метода PUT v1/account/email')
@allure.sub_suite('Позитивные тесты')
class TestsPutV1AccountEmail:
    @allure.title('Проверка смены email пользователя')
    def test_put_v1_account_email(
            self,
            account_helper,
            prepare_user
            ):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email

        # Регистрация пользователя
        response = account_helper.register_new_user(login=login, password=password, email=email)
        PutV1AccountEmail.check_response_values(response)
        print(response)

        # Авторизоваться
        account_helper.user_login(login=login, password=password)

        # Смена email
        response = account_helper.change_email(login=login, password=password, email=email)
        PutV1AccountEmail.check_response_values(response)
        print(response)

        # Авторизация под старыми данными неудачная
        with check_status_code_http(403, 'User is inactive. Address the technical support for more details'):
            account_helper.user_login(login=login, password=password)

        # Получить токен из почтового сервера по новому email для подтверждения смены
        token = account_helper.get_token_by_login(login=login, token_type='activation')
        response = account_helper.activate_user(token=token)
        PutV1AccountEmail.check_response_values(response)
        print(response)

        # Авторизоваться
        with check_status_code_http():
            account_helper.user_login(login=login, password=password)
