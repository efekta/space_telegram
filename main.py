from send_telegram import send_telegram
from fetch_nasa import upload_image_nasa
from fetch_nasa_epic import upload_image_epic
from fetch_spacex import fetch_spacex_last_launch
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
            upload_image_epic()
            upload_image_nasa()
            fetch_spacex_last_launch()
            send_telegram()
        else:
            print('Некорректный ввод!')
    except requests.exceptions.HTTPError:
        print('Некорректный ввод!')


if __name__ == '__main__':
    main()
