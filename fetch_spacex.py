import requests
from download_picture import download_picture
from find_extension_file import find_extension_file

def fetch_spacex_last_launch(directory):
    path_picture = directory
    url_spacex = 'https://api.spacexdata.com/v4/rockets'
    response = requests.get(url_spacex)
    response.raise_for_status()
    response_links = response.json()

    for item in response_links:
        spacex_link = item['flickr_images']

    for link_number, link in enumerate(spacex_link):
        find_extension = find_extension_file(link)
        file_name = f'spacex_{link_number}{find_extension}'
        picture_path = f'{path_picture}/{file_name}'

        download_picture(url=link,
                          payload='',
                          path_picture=picture_path)
