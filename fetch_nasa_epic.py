import requests
import os.path
from datetime import datetime
from dotenv import load_dotenv

def upload_image_epic():
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    url_nasa_epic = f'https://api.nasa.gov/EPIC/api/natural/'
    payload_epic = {'api_key': nasa_token}
    epic_nasa_links = []
    response_nasa_epic = requests.get(url_nasa_epic, params=payload_epic)
    response_nasa_epic.raise_for_status()
    response_nasa_epic_links = response_nasa_epic.json()

    for item in response_nasa_epic_links:
        date_item = item['date']
        date_time = datetime.fromisoformat(date_item)
        date = date_time.date()
        now_date = date.strftime("%Y/%m/%d")
        image_name = item['image']
        format_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                     f'{now_date}/png/{image_name}.png?api_key={nasa_token}'
        epic_nasa_links.append(format_url)

    return epic_nasa_links

    # for epic_link_number, epic_link in enumerate(epic_nasa_links):
    #     image_name = f'nasa_epic{epic_link_number}.png'
    #     print(image_name) # создала имена картинкам
        # response_nasa = requests.get(epic_link, params=payload_epic)
        # print(response_nasa)
        # response_nasa.raise_for_status()
        # print(response_nasa)

        # with open(f'{path_img}{image_name}', 'wb') as file:
        #     file.write(response_nasa.content)
upload_image_epic()