import requests

def download_picture(url: str, payload: str, path_picture: str):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(path_picture, 'wb') as file:
        file.write(response.content)
