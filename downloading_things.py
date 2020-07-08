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
    try:
        download_it(*argv[1:])
    except TypeError:
        print("\n\nThe download function works with only 2 arguments:\n"
              "\turl: The url you want to request a file.\n"
              "\tfilename: a str argument that accepts the file name (obviously).\n\n"
              "Syntax:\n"
              f"\tpython downloading_things.py <https:\\www.Something_cOoL>.com> yay.anything")
