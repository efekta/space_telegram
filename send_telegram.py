import os.path
from os import listdir
import telegram
from dotenv import load_dotenv
import time
import random

load_dotenv()
tg_token = os.getenv('TG_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')
channel_id = os.getenv('CHANEL_ID')
sleep_time_test = 5
sleep_time = 86400

def send_telegram():
    while True:
        photos_list = listdir('images')

        with open(f'images/{random.choice(photos_list)}', 'rb') as file:
            bot = telegram.Bot(token=tg_token)
            bot.send_photo(chat_id=tg_chat_id,
                           photo=file)
            time.sleep(sleep_time_test)