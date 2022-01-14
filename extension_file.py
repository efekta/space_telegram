import os
from urllib.parse import urlsplit

def extension_file(link):
    extension_link = urlsplit(link)
    url_path = extension_link.path
    extension_link = os.path.splitext(url_path)[-1]
    return extension_link

# TODO UPLOAD_PICTURES
file_extension = extension_file('https://example.com/txt/hello%20world.txt?v=9#python')