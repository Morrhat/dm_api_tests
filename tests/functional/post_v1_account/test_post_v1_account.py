import allure
import pytest
from checkers.http_checkers import check_status_code_http


@allure.suite('Тесты на проверку метода POST v1/account')
@allure.sub_suite('Позитивные тесты')
class TestsPostV1Account:
    @allure.title('Проверка регистрации нового пользователя')
    def test_post_v1_account(
            self,
            account_helper,
            prepare_user
            ):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email

        # Регистрация пользователя
        account_helper.register_new_user(login=login, password=password, email=email)



data = [
    # Короткий пароль: менее 6 символов
    {
        'login': 'kristinochka_09_11_2025_18_00_03',
        'email': 'kristinochka_09_11_2025_18_00_03@mail.com',
        'password': '42'
    },
    # Невалидный емейл: например, без использования символа @
{
        'login': 'kristinochka_09_11_2025_18_00_03',
        'email': 'krismail.com',
        'password': '123456789'
    },
    #  Невалидный логин: например, один символ
{
        'login': 'k',
        'email': 'kristinochka_09_11_2025_18_00_03@mail.com',
        'password': '123456789'
    }
]


@allure.suite('Тесты на проверку метода POST v1/account')
@allure.sub_suite('Негативные тесты')
class TestsPostV1AccountNegative:
    @allure.title('Проверка регистрации нового пользователя')
    @pytest.mark.parametrize('data', data)
    def test_post_v1_account_negative(
            self,
            account_helper,
            data
            ):
        # Регистрация пользователя
        with check_status_code_http(400, 'Validation failed'):
            account_helper.register_new_user(login=data['login'], password=data['password'], email=data['email'])