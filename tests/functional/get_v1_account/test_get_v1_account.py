from datetime import datetime

import pytest
from hamcrest import (
    assert_that,
    has_property,
    starts_with,
    all_of,
    instance_of,
    has_properties,
    equal_to,
)
from checkers.http_checkers import check_status_code_http


# Текущий пользователь через авторизованный клиент
@pytest.mark.order(1)
def test_get_v1_account(
        auth_account_helper
):
    with check_status_code_http():
        response = auth_account_helper.get_account_info()
    print(response)
    assert_that(
        response, all_of(
            has_property('resource', has_property('login', starts_with('kristinochka'))),
            has_property('resource', has_property('registration', instance_of(datetime))),
            has_property(
                'resource', has_properties(
                    {
                        'roles': ["Guest", "Player"]
                    }
                    )
                ),
            has_property('resource', has_property('info', equal_to(""))),
            has_property('resource', has_property("settings", has_property('color_schema', equal_to(None)))),
            has_property('resource', has_property("settings", has_property('nanny_greetings_message', equal_to(None)))),
            has_property(
                'resource', has_property(
                    "settings", has_property(
                        'paging', has_properties(
                            {
                                "posts_per_page": equal_to(10),
                                "comments_per_page": equal_to(10),
                                "topics_per_page": equal_to(10),
                                "messages_per_page": equal_to(10),
                                "entities_per_page": equal_to(10)
                            }
                        )
                        )
                    )
                )
        )
    )


 #Текущий пользователь без авторизации
def test_get_v1_account_no_auth(
        account_helper,
        validate_response=False
):
    with check_status_code_http(401, 'User must be authenticated'):
        account_helper.get_account_info(validate_response=validate_response)
