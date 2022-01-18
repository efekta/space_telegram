import requests
from datetime import datetime
from download_picture import download_picture
from get_file_extension import get_file_extension


def fetch_nasa_apod(payload_nasa, directory):
    base_url = f'https://api.nasa.gov/planetary/apod'
    response_nasa = requests.get(base_url, params=payload_nasa)
    response_nasa.raise_for_status()
    response_nasa = response_nasa.json()
    for link_number, link in enumerate(response_nasa):
        link = link['url']
        find_extension = get_file_extension(link)
        file_name = f'planetary_{link_number}{find_extension}'
        picture_path = f'{directory}/{file_name}'
        download_picture(
            url=link, payload=payload_nasa, path_picture=picture_path)


def fetch_nasa_epic(directory, payload_epic):
    base_url = f'https://api.nasa.gov/EPIC/api/natural/'
    response = requests.get(base_url, params=payload_epic)
    response.raise_for_status()
    response_nasa = response.json()
    for item in response_nasa:
        date_item = item['date']
        date_time = datetime.fromisoformat(date_item)
        date = date_time.date()
        now_date = date.strftime("%Y/%m/%d")
        image_name = item['image']
        find_extension = '.png'
        format_url = f'https://api.nasa.gov/EPIC/archive/natural/{now_date}' \
            f'/png/{image_name}{find_extension}'
        file_name = f'{image_name}{find_extension}'
        picture_path = f'{directory}/{file_name}'
        download_picture(
            url=format_url, payload=payload_epic, path_picture=picture_path)
