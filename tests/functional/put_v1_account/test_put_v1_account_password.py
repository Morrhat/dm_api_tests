

def test_put_v1_account_password(account_helper, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    # Регистрация пользователя
    account_helper.register_new_user(login=login, password=password, email=email)

    # Авторизоваться
    account_helper.user_login(login=login, password=password)

    # Начало сброса пароля
    account_helper.change_password(login=login, email=email, password=password)

    token = account_helper.get_password_token(login=login)

    # Смена пароля
    account_helper.set_new_password(login=login, password=password, token=token)

    # Авторизоваться с новым паролем
    account_helper.user_login(login=login, password="987654321")

