from restclient.configuration import Configuration
from dm_api_account.apis.account_api import AccountAPI
from dm_api_account.apis.login_api import LoginAPI


class DMApiAccount:
    def __init__(
            self,
            configuration: Configuration
    ):
        self.configuration = configuration
        self.login_api = LoginAPI(configuration=configuration)
        self.account_api = AccountAPI(configuration=configuration)
