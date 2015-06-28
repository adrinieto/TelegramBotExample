import json
import urllib2
from config import TOKEN


class TelegramBot(object):
    def __init__(self):
        self.base_url = "https://api.telegram.org/bot" + TOKEN + "/"

    def get_me(self):
        response = json.load(urllib2.urlopen(self.base_url + "getMe"))
        return response['ok']


bot = TelegramBot()
print bot.get_me()
