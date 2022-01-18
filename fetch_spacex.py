import requests
from download_picture import download_picture
from get_file_extension import get_file_extension


def fetch_spacex_last_launch(directory):
    url_spacex = 'https://api.spacexdata.com/v4/rockets'
    response = requests.get(url_spacex)
    response.raise_for_status()
    response_links = response.json()
    for item in response_links:
        spacex_link = item['flickr_images']
    for link_number, link in enumerate(spacex_link):
        file_extension = get_file_extension(link)
        file_name = f'spacex_{link_number}{file_extension}'
        picture_path = f'{directory}/{file_name}'
        download_picture(url=link, payload='', path=picture_path)

