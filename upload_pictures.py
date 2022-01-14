import requests
from pathlib import Path

path_img = 'images/'
Path('images').mkdir(parents=True, exist_ok=True)

def upload_pictures(url, payload, path_img):

    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(path_img, 'wb') as picture_file:
        picture_file.write(response.content)

    # for link_number, link in enumerate(links):
    #     image_name = f'spacex{link_number}.jpg'
    #     response_spacex = requests.get(link)
    #     response_spacex.raise_for_status()
    #     with open(f'{path_img}{image_name}', 'wb') as file:
    #         file.write(response_spacex.content)

    # with open(f'{path_img}{image_name}', 'wb') as file:
    #     file.write(response_spacex.content)

