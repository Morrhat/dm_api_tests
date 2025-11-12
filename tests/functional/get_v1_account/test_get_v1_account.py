import allure
import pytest

from checkers.get_v1_account import GetV1Account
from checkers.http_checkers import check_status_code_http


# Текущий пользователь через авторизованный клиент
@allure.suite('Тесты на проверку метода GET v1/account')
@allure.sub_suite('Позитивные тесты')
class TestsGetV1Account:
    @allure.title('Проверка получения данных пользователя')
    @pytest.mark.order(1)
    def test_get_v1_account(
            self,
            auth_account_helper
    ):
        with check_status_code_http():
            response = auth_account_helper.get_account_info()
        GetV1Account.check_response_values(response)
        print(response)


    #Текущий пользователь без авторизации
@allure.suite('Тесты на проверку метода GET v1/account')
@allure.sub_suite('Негативные тесты')
class TestsGetV1AccountNegative:
    @allure.title('Проверка получения данных пользователя')
    def test_get_v1_account_no_auth(
            self,
            account_helper,
            validate_response=False
    ):
        with check_status_code_http(401, 'User must be authenticated'):
            account_helper.get_account_info(validate_response=validate_response)
