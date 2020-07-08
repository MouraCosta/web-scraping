import requests
from sys import argv


def download_it(url, filename: str):
    response = requests.get(url)

    # Treats if the url doesnt exists.
    try:
        response.raise_for_status()
    except Exception:
        print("The requested url does not exist.")

    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    download_it(*argv[1:])
