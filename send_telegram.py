import os.path
from os import listdir
import telegram
import time
import random

def send_telegram():
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    sleep_time_test = 5
    while True:
        photos_list = listdir('images')

        with open(f'images/{random.choice(photos_list)}', 'rb') as file:
            bot = telegram.Bot(token=tg_token)
            bot.send_photo(chat_id=tg_chat_id, photo=file)
            time.sleep(sleep_time_test)