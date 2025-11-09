from checkers.http_checkers import check_status_code_http
from assertpy import assert_that, soft_assertions
from dm_api_account.models.user_details_envelope import UserRole


def test_put_v1_account_email(
        account_helper,
        prepare_user
        ):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    # Регистрация пользователя
    response = account_helper.register_new_user(login=login, password=password, email=email)
    with soft_assertions():
        assert_that(response.resource.login).starts_with('kristinochka')
        assert_that(response.resource.roles).contains(UserRole.GUEST, UserRole.PLAYER)
        print('Прошла регистрация и активация')

    # Авторизоваться
    account_helper.user_login(login=login, password=password)

    # Смена email
    response = account_helper.change_email(login=login, password=password, email=email)
    with soft_assertions():
        assert_that(response.resource.login).starts_with('kristinochka')
        assert_that(response.resource.roles).contains(UserRole.GUEST, UserRole.PLAYER)
        print('Прошла смена email')

    # Авторизация под старыми данными неудачная
    with check_status_code_http(403, 'User is inactive. Address the technical support for more details'):
        response = account_helper.user_login(login=login, password=password)
        with soft_assertions():
            assert_that(response.resource.title).is_equal_to('User is inactive. Address the technical support for more details')

    # Получить токен из почтового сервера по новому email для подтверждения смены
    token = account_helper.get_token_by_login(login=login, token_type='activation')
    response = account_helper.activate_user(token=token)
    with soft_assertions():
        assert_that(response.resource.login).starts_with('kristinochka')
        assert_that(response.resource.roles).contains(UserRole.GUEST, UserRole.PLAYER)
        print('Прошла активация с новым email')


    # Авторизоваться
    with check_status_code_http():
        account_helper.user_login(login=login, password=password)
