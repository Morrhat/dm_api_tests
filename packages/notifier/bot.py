import os
from pathlib import Path

from telebot import TeleBot
from telegram_notifier.exceptions import TelegramNotifierError
from vyper import v

config = Path(__file__).parent.joinpath('../../').joinpath('config')
v.set_config_name('prod')
v.add_config_path(config)
v.read_in_config()

os.environ['TELEGRAM_BOT_CHAT_ID'] = v.get('telegram.chat_id')
os.environ['TELEGRAM_BOT_ACCESS_TOKEN'] = v.get('telegram.token')


class TelegramBot:
    def __init__(self) -> None:
        if chat_id := os.getenv('TELEGRAM_BOT_CHAT_ID'):
            self._chat_id = int(chat_id)
        else:
            raise TelegramNotifierError('Need present environment variable "TELEGRAM_BOT_CHAT_ID"!')
        if access_token := os.getenv('TELEGRAM_BOT_ACCESS_TOKEN'):
            self._telegram_bot = TeleBot(access_token)
        else:
            raise TelegramNotifierError('Need present environment variable "TELEGRAM_BOT_ACCESS_TOKEN"!')


    def send_file(self) -> None:
        file_path = Path(__file__).parent.joinpath('swagger-coverage-dm-api-account.html')
        with open(file_path, 'rb') as document:
            self._telegram_bot.send_document(
                self._chat_id,
                document=document,
                caption='coverage',
            )

