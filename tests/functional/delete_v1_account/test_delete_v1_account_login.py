# Выход из аккаунта авторизованным клиентом
def test_delete_v1_account(
        auth_account_helper
        ):
    auth_account_helper.logout_user()

    # Выход из аккаунта без авторизации клиента
def test_delete_v1_account_no_auth(
        account_helper
        ):
    account_helper.logout_user_all()
