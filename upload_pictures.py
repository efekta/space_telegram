import requests
from fetch_spacex import fetch_spacex_last_launch
from pathlib import Path


def upload_pictures():
    fetch_spacex_last_launch()
    path_img = 'images/'
    Path('images').mkdir(parents=True, exist_ok=True)
    for link_number, link in enumerate(fetch_spacex_last_launch()):
        image_name = f'spacex{link_number}.jpg'
        response_spacex = requests.get(link)
        response_spacex.raise_for_status()
        with open(f'{path_img}{image_name}', 'wb') as file:
            file.write(response_spacex.content)

    with open(f'{path_img}{image_name}', 'wb') as file:
        file.write(response_spacex.content)

upload_pictures()
