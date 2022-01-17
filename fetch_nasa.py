import requests
from extension_file import extension_file
from download_picture import download_picture

def upload_image_nasa(payload_nasa, directory):
    url_nasa = f'https://api.nasa.gov/planetary/apod'
    path_picture = directory
    response_nasa = requests.get(url_nasa, params=payload_nasa)
    response_nasa.raise_for_status()
    response_nasa = response_nasa.json()

    for link_number, link in enumerate(response_nasa):
        link = link['url']
        extension_file_name = extension_file(link)
        file_name = f'planetary_{link_number}{extension_file_name}'
        picture_path = f'{path_picture}/{file_name}'

        download_picture(url=link,
                          payload=payload_nasa,
                          path_picture=picture_path)



