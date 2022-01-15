import requests
from download_pictures import download_pictures
from extension_file import extension_file

def fetch_spacex_last_launch(directory):
    path_pictures = directory
    url_spacex = 'https://api.spacexdata.com/v4/rockets'
    response_spacex = requests.get(url_spacex)
    response_spacex.raise_for_status()
    response_spacex_links = response_spacex.json()

    for item in response_spacex_links:
        spacex_link = item['flickr_images']

    for link_number, link in enumerate(spacex_link):
        extension_file_name = extension_file(link)
        file_name = f'spacex_{link_number}{extension_file_name}'
        picture_path = f'{path_pictures}/{file_name}'

        download_pictures(url=link,
                          payload='',
                          path_pictures=picture_path)
