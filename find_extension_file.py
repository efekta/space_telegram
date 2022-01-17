import os
from urllib.parse import urlsplit

def find_extension_file(link):
    extension_link = urlsplit(link)
    url_path = extension_link.path
    extension_link = os.path.splitext(url_path)[-1]
    return extension_link
