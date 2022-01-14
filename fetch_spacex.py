import requests
from pathlib import Path

def fetch_spacex_last_launch():
    url_spacex = 'https://api.spacexdata.com/v4/rockets'
    # path_img = 'images/'
    # Path('images').mkdir(parents=True, exist_ok=True)
    spacex_links = []
    response_spacex = requests.get(url_spacex)
    response_spacex.raise_for_status()
    response_spacex_links = response_spacex.json()

    for item in response_spacex_links:
        item_link = item['flickr_images']
        for link in item_link:
            spacex_links.append(link)

    return spacex_links

# spacex_links = fetch_spacex_last_launch()

    # for link_number, link in enumerate(spacex_links):
    #     image_name = f'spacex{link_number}.jpg'
    #     response_spacex = requests.get(link)
    #     response_spacex.raise_for_status()
    #     with open(f'{path_img}{image_name}', 'wb') as file:
    #         file.write(response_spacex.content)