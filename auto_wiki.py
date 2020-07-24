#! usr/bin/python3

import sys
import os

import requests
from bs4 import BeautifulSoup

# TODO: Criando um diretório pra cada resultado encontrado
if (query_path := ' '.join(sys.argv[1:])) in os.listdir("./"):
    os.chdir(f"./{query_path}")
else:
    os.mkdir(query_path)
    os.chdir(f"./{query_path}")

# TODO: Fazendo download do site do wikipedia
query = query_path.capitalize()
req = requests.get(f"https://pt.wikipedia.org/wiki/{query}")
req.raise_for_status()

# TODO: Fazendo parse no HTML presente no site e extrai o conteúdo 
# para um arquivo
soup = BeautifulSoup(req.text, "html.parser")


def make_file(filename=query+".txt"):
    """Create a file about topic requested in wikipedia"""
    global soup
    with open(filename, "w") as topic_file:
        for p_tag in soup.find_all("p"):
            topic_file.write(p_tag.get_text())


make_file()
