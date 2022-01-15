import requests
from datetime import datetime
from extension_file import extension_file
from download_pictures import download_pictures

def upload_image_epic(directory, payload_epic, nasa_token):
    path_pictures = directory
    url_nasa_epic = f'https://api.nasa.gov/EPIC/api/natural/'
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
        extension_file_name = extension_file(format_url)
        file_name = f'{image_name}{extension_file_name}'
        picture_path = f'{path_pictures}/{file_name}'

        download_pictures(url=format_url,
                          payload=nasa_token,
                          path_pictures=picture_path)
