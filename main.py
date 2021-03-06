import os
import time
import requests
import telegram
from pathlib import Path
from dotenv import load_dotenv
from fetch_nasa import fetch_nasa_apod
from fetch_nasa import fetch_nasa_epic
from fetch_spacex import fetch_spacex_last_launch


def send_telegram(tg_token: str, tg_chat_id: str, picture_path: str):
    bot = telegram.Bot(tg_token)
    with open(picture_path, 'rb') as picture:
        bot.send_photo(chat_id=tg_chat_id, photo=picture)


def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    channel_id = os.getenv('CHANEL_ID')
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    delay_seconds = int(os.getenv('DELAY_SECONDS'))
    directory = 'images'
    count = 30
    Path('images').mkdir(parents=True, exist_ok=True)
    payload_nasa = {'api_key': nasa_token, 'count': count}
    payload_epic = {'api_key': nasa_token}
    try:
        fetch_spacex_last_launch(directory)
        fetch_nasa_apod(payload_nasa, directory)
        fetch_nasa_epic(directory, payload_epic)
    except requests.models.HTTPError:
        print('Некорректный ответ сервера')
    while True:
        for picture_name in os.listdir(directory):
            picture_path = os.path.join(directory, picture_name)
            send_telegram(tg_token, channel_id, picture_path)
            time.sleep(delay_seconds)


if __name__ == '__main__':
    main()
