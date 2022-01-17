import requests
from download_picture import download_picture
from find_extension_file import find_extension_file


def fetch_image_nasa(payload_nasa, directory):
    url_nasa = f'https://api.nasa.gov/planetary/apod'
    response_nasa = requests.get(url_nasa, params=payload_nasa)
    response_nasa.raise_for_status()
    response_nasa = response_nasa.json()
    for link_number, link in enumerate(response_nasa):
        link = link['url']
        find_extension = find_extension_file(link)
        file_name = f'planetary_{link_number}{find_extension}'
        picture_path = f'{directory}/{file_name}'
        download_picture(
            url=link, payload=payload_nasa, path_picture=picture_path)
