import os.path
from os import listdir
import telegram
import time
import random

from dotenv import load_dotenv

load_dotenv()
tg_token = os.getenv('TG_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')
delay_seconds = os.getenv('DELAY_SECONDS')

def send_telegram():

    while True:
        pictures = listdir('images')

        with open(f'images/{random.choice(pictures)}', 'rb') as file:
            bot = telegram.Bot(token=tg_token)
            bot.send_photo(chat_id=tg_chat_id, photo=file)
            time.sleep(int(delay_seconds))
send_telegram()