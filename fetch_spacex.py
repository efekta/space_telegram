import requests
from extension_file import extension_file
from upload_pictures import upload_pictures

def fetch_spacex_last_launch():
    url_spacex = 'https://api.spacexdata.com/v4/rockets'
    response_spacex = requests.get(url_spacex)
    response_spacex.raise_for_status()
    response_spacex_links = response_spacex.json()
    for item in response_spacex_links:
        spacex_links = item['flickr_images']
    for link_number, link in enumerate(spacex_links):
        image_name = f'spacex{link_number}.jpg'
        response_spacex = requests.get(link)
        response_spacex.raise_for_status()

        # upload_pictures(
        #     url=url,
        #     payload='',
        #     picture_path=path_img,
        # )


    # for link_number, link in enumerate(spacex_links):
    #     image_name = f'spacex{link_number}.jpg'
    #     response_spacex = requests.get(link)
    #     response_spacex.raise_for_status()
    #     with open(f'{path_img}{image_name}', 'wb') as file:
    #         file.write(response_spacex.content)

