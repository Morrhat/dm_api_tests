
def test_get_v1_account(auth_account_helper):
    auth_account_helper.get_account_info()

def test_get_v1_account_no_auth(account_helper):
    account_helper.get_account_info()

