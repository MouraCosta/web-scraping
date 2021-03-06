import requests
from requests import HTTPError
from sys import argv


def download_it(url, filename: str):
    request = requests.get(url)

    # Treats if the url doesnt exists.
    try:
        request.raise_for_status()
    except HTTPError:
        print("The requested url does not exist.")
    
    # Make the file
    with open(filename, 'wb') as file:
        file.write(request.content)


if __name__ == '__main__':
    try:
        download_it(*argv[1:])
    except TypeError:
        print("\033[;33m\n\nThe download function works with only 2 arguments:\n"
              "\turl: The url you want to request a file.\n"
              "\tfilename: a str argument that accepts the file name (obviously).\n\n"
              "Syntax:\n"
              f"\tpython get_file.py <https:\\www.Something_cOoL>.com> yay.anything\033[m")
