import requests
from download_picture import download_picture
from find_extension_file import find_extension_file

def fetch_spacex_last_launch(directory):
    path_picture = directory
    url_spacex = 'https://api.spacexdata.com/v4/rockets'
    response_spacex = requests.get(url_spacex)
    response_spacex.raise_for_status()
    response_spacex_links = response_spacex.json()

    for item in response_spacex_links:
        spacex_link = item['flickr_images']

    for link_number, link in enumerate(spacex_link):
        find_extension_file_name = find_extension_file(link)
        file_name = f'spacex_{link_number}{find_extension_file_name}'
        picture_path = f'{path_picture}/{file_name}'

        download_picture(url=link,
                          payload='',
                          path_picture=picture_path)
