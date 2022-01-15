import requests

def download_pictures(url: str, payload: str, path_pictures: str):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(path_pictures, 'wb') as file:
        file.write(response.content)
