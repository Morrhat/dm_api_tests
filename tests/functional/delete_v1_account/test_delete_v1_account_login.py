# Выход из аккаунта авторизованным клиентом
import allure

from checkers.http_checkers import check_status_code_http

@allure.suite('Тесты на проверку метода DELETE v1/account')
@allure.sub_suite('Позитивные тесты')
class TestsDeleteV1Account:
    @allure.title('Проверка Выхода из аккаунта пользователя')
    def test_delete_v1_account(
            self,
            auth_account_helper
            ):
        auth_account_helper.logout_user()



    # Выход из аккаунта без авторизации клиента
@allure.suite('Тесты на проверку метода DELETE v1/account')
@allure.sub_suite('Негативные тесты')
class TestsDeleteV1AccountNegative:
    @allure.title('Проверка Выхода из аккаунта пользователя')
    def test_delete_v1_account_no_auth(
            self,
            account_helper
            ):
        with check_status_code_http(401, 'User must be authenticated'):
            account_helper.logout_user()
