import requests

from dm_api_account.models.registration import Registration
from dm_api_account.models.user_envelope import UserEnvelope
from restclient.client import RestClient


class AccountAPI(RestClient):

    def post_v1_account(
            self,
            registration: Registration,
    ):
        """
        POST
        /v1/account
        Register new user
        :param json_data:
        :return:
        """

        response = self.post(
            path=f'/v1/account',
            json=registration.model_dump(exclude_none=True, by_alias=True)
        )
        return response

    def get_v1_account(
            self,
            **kwargs
    ):
        """
        GET
        /v1/account
        Get current user
        :return:
        """

        response = self.get(
            path=f'/v1/account',
            **kwargs
        )
        return response

    def put_v1_account_token(
            self,
            token,
            validate_response=True
    ):
        """
        PUT
        /v1/account/{token}
        Activate registered user
        :param validate_response:
        :param token:
        :return:
        """

        headers = {
            'accept': 'text/plain',
        }
        response = self.put(
            path=f'/v1/account/{token}',
            headers=headers
        )
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_email(
            self,
            json_data
    ):
        """
        PUT
        /v1/account/email
        Change registered user email
        :return:
        """

        headers = {
            'accept': 'text/plain'
        }
        response = self.put(
            path=f'/v1/account/email',
            json=json_data,
            headers=headers
        )
        return response

    def post_v1_account_password(
            self,
            json_data
    ):
        """
        POST
        /v1/account/password
        Reset registered user password
        :return:
        """

        headers = {
            'accept': 'text/plain'
        }
        response = self.post(
            path=f'/v1/account/password',
            json=json_data,
            headers=headers
        )
        return response

    def put_v1_account_password(
            self,
            json_data
    ):
        """
        PUT
        /v1/account/password
        Change registered user password
        :param json_data:
        :return:
        """

        headers = {
            'accept': 'text/plain'
        }
        response = self.put(
            path=f'/v1/account/password',
            json=json_data,
            headers=headers
        )
        return response
