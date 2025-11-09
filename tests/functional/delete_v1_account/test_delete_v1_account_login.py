# Выход из аккаунта авторизованным клиентом
from checkers.http_checkers import check_status_code_http


def test_delete_v1_account(
        auth_account_helper
        ):
    auth_account_helper.logout_user()

    # Выход из аккаунта без авторизации клиента
def test_delete_v1_account_no_auth(
        account_helper
        ):
    with check_status_code_http(401, 'User must be authenticated'):
        account_helper.logout_user_all()
