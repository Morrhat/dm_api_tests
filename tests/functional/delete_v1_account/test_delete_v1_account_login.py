
def test_delete_v1_account(auth_account_helper):
    # Выход из аккаунта авторизованным клиентом
    auth_account_helper.dm_account_api.login_api.delete_v1_account_login()

    # Выход из аккаунта без авторизации клиента
def test_delete_v1_account_no_auth(account_helper):
    account_helper.dm_account_api.login_api.delete_v1_account_login()