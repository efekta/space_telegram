import requests


def download_picture(url: str, payload, path: str):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)
