def test_put_v1_account_email(
        account_helper,
        prepare_user
        ):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    # Регистрация пользователя
    account_helper.register_new_user(login=login, password=password, email=email)

    # Авторизоваться
    account_helper.user_login(login=login, password=password)

    # Смена email
    account_helper.change_email(login=login, password=password, email=email)

    # Авторизация под старыми данными неудачная
    #response = account_helper.user_login(login=login, password=password)
    #assert response.status_code == 403, f"Пользователь смог авторизоваться под старыми данными {response.json()}"

    # Получить токен из почтового сервера по новому email для подтверждения смены
    token = account_helper.get_token_by_login(login=login, token_type='activation')
    account_helper.activate_user(token=token)


    # Авторизоваться
    response = account_helper.user_login(login=login, password=password)
    assert response.status_code == 200, f"Пользователь не смог авторизоваться {response.json()}"
