
def test_delete_v1_account_all(auth_account_helper):
    # Выход из всех аккаунтов авторизованным клиентом
    auth_account_helper.dm_account_api.login_api.delete_v1_account_login_all()


    # Выход из всех аккаунтов без авторизации клиента
def test_delete_v1_account_no_auth(account_helper):
    account_helper.dm_account_api.login_api.delete_v1_account_login_all()