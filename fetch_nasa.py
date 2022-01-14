import requests
import os.path
from pathlib import Path
from dotenv import load_dotenv

def upload_image_nasa():
    count = 30
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    # path_img = 'images/'
    # Path('images').mkdir(parents=True, exist_ok=True)
    url_nasa = f'https://api.nasa.gov/planetary/apod'
    payload_nasa = {'api_key': nasa_token, 'count': count}
    nasa_links = []
    response_nasa = requests.get(url_nasa, params=payload_nasa)
    response_nasa.raise_for_status()
    response_nasa = response_nasa.json()

    for link in response_nasa:
        link = link['url']
        nasa_links.append(link)

    return nasa_links

upload_image_nasa()
    # for link_number, link in enumerate(nasa_links):
    #     image_name = f'nasa{link_number}.jpg'
    #     response_nasa = requests.get(link)
    #     response_nasa.raise_for_status()
    #     with open(f'{path_img}{image_name}', 'wb') as file:
    #         file.write(response_nasa.content)


