# encoding: utf-8
import json
from pprint import pprint
from time import sleep
import urllib
import urllib2
from config import TOKEN


class TelegramBot(object):
    def __init__(self):
        self.base_url = "https://api.telegram.org/bot" + TOKEN + "/"
        self.offset = 0

    def get_me(self):
        response = json.load(urllib2.urlopen(self.base_url + "getMe"))
        return response['ok']

    def get_updates(self):
        data = {
            "offset": self.offset
        }
        response = json.load(urllib2.urlopen(self.base_url + "getUpdates", urllib.urlencode(data)))
        if len(response['result']) > 0:
            self.offset = response['result'][-1]['update_id'] + 1
        return response['result']

    def send_message(self, msg, chat_id, reply_id=None):
        data = {
            "chat_id": chat_id,
            "text": msg,
        }
        if reply_id is not None:
            data["reply_to_message_id"] = reply_id
        response = json.load(urllib2.urlopen(self.base_url + "sendMessage", urllib.urlencode(data)))
        #pprint(response)


def polling():
    bot = TelegramBot()
    print bot.get_me()

    while True:
        for in_message in bot.get_updates():
            #pprint(in_message)
            message = in_message['message']
            bot.send_message(message['text'], message['chat']['id'], message['message_id'])
        sleep(2)


if __name__ == "__main__":
    polling()
