
def test_delete_v1_account(account_helper, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    # Регистрация пользователя
    account_helper.register_new_user(login=login, password=password, email=email)

    # Авторизоваться
    account_helper.auth_client(login=login, password=password)

    # Выход из аккаунта

    account_helper.dm_account_api.login_api.delete_v1_account_login()