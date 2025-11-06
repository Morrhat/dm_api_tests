# Текущий пользователь через авторизованный клиент
def test_get_v1_account(
        auth_account_helper
        ):
    auth_account_helper.get_account_info()

# Текущий пользователь без авторизации
def test_get_v1_account_no_auth(
        account_helper,
        validate_response=False
        ):
    account_helper.get_account_info(validate_response=False)
