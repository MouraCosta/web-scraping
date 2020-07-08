import requests
from sys import argv


def download_it(url, filename: str):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)


if __name__ == '__main__':
    download_it(*argv[1:])
