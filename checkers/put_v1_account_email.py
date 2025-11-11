from hamcrest import (
    assert_that,
    all_of,
    has_property,
    has_properties,
    starts_with,
)



class PutV1AccountEmail:
    @classmethod
    def check_response_values(
            cls,
            response
    ):
        assert_that(
            response, all_of(
                has_property('resource', has_property('login', starts_with('kristinochka'))),
                has_property(
                    'resource', has_properties(
                        {
                            'roles': ["Guest", "Player"]
                        }
                    )
                )
            )
        )