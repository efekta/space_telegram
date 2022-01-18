import requests


def download_picture(url: str,  path: str, payload=''):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)
