"""A função desse script é abrir uma página na internet 
com os parâmetros de localização"""

import webbrowser
import sys

if len(sys.argv) <= 1:
    raise TypeError("You must input a str place name.")

address = f'https://www.google.com.br/maps/place/' \
          f'{"+".join(sys.argv[1:])}'
webbrowser.open(address)
