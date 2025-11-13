import allure


@allure.suite('Тесты на проверку метода PUT v1/account/password')
@allure.sub_suite('Позитивные тесты')
class TestsPutV1AccountPassword:
    @allure.title('Проверка смены пароля пользователя')
    def test_put_v1_account_password(self, account_helper, prepare_user):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email

        # Регистрация пользователя
        account_helper.register_new_user(login=login, password=password, email=email)

        # Авторизоваться
        account_helper.user_login(login=login, password=password)

        #Выбор нового пароля
        new_password = "987654321"

        # Смена пароля
        account_helper.change_password(login=login, email=email, password=password, new_password=new_password)

        # Авторизоваться с новым паролем
        account_helper.user_login(login=login, password=new_password)

