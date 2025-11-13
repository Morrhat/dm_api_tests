# Выход из всех аккаунтов авторизованным клиентом
import allure

from checkers.http_checkers import check_status_code_http

@allure.suite('Тесты на проверку метода DELETE v1/account/all')
@allure.sub_suite('Позитивные тесты')
class TestsDeleteV1AccountAll:
    @allure.title('Проверка Выхода из всех аккаунтов пользователя')
    def test_delete_v1_account_all(
            self,
            auth_account_helper
            ):
        auth_account_helper.logout_user_all()



    # Выход из всех аккаунтов без авторизации клиента
@allure.suite('Тесты на проверку метода DELETE v1/account/all')
@allure.sub_suite('Негативные тесты')
class TestsDeleteV1AccountAllNegative:
    @allure.title('Проверка Выхода из всех аккаунтов пользователя')
    def test_delete_v1_account_no_auth(
            self,
            account_helper
            ):
        with check_status_code_http(401, 'User must be authenticated'):
            account_helper.logout_user_all()
