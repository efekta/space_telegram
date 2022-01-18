import os
from urllib.parse import urlsplit


def get_file_extension(link):
    file_extension = urlsplit(link)
    url_path = file_extension.path
    file_extension = os.path.splitext(url_path)[-1]
    return file_extension
