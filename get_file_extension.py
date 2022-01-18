import os
from urllib.parse import urlsplit


def get_file_extension(link):
    extension_path = urlsplit(link)
    url_path = extension_path.path
    extension_path = os.path.splitext(url_path)[-1]
    return extension_path
