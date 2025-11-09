import pytest

from checkers.get_v1_account import GetV1Account
from checkers.http_checkers import check_status_code_http


# Текущий пользователь через авторизованный клиент
@pytest.mark.order(1)
def test_get_v1_account(
        auth_account_helper
):
    GetV1Account.check_response_values(auth_account_helper)


#Текущий пользователь без авторизации
def test_get_v1_account_no_auth(
        account_helper,
        validate_response=False
):
    with check_status_code_http(401, 'User must be authenticated'):
        account_helper.get_account_info(validate_response=validate_response)
