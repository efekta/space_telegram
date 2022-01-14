from send_telegram import send_telegram
from fetch_nasa import upload_image_nasa
from fetch_nasa_epic import upload_image_epic
from fetch_spacex import fetch_spacex_last_launch
from upload_pictures import upload_pictures
from extension_file import extension_file
import os
import argparse
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    channel_id = os.getenv('CHANEL_ID')
    parser = argparse.ArgumentParser(description='Описание программы')
    parser.add_argument('link', type=str, help='CHANEL_ID')
    args = parser.parse_args()
    args_channel_id = args.link

    try:
        if args_channel_id == channel_id:

            spacex_links = fetch_spacex_last_launch()
            extension_path = extension_file()
            upload_pictures(spacex_links)

    except requests.models.HTTPError:
        print('Некорректный ответ сервера')


if __name__ == '__main__':
    main()
