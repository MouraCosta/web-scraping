import sys
import webbrowser
import requests
from bs4 import BeautifulSoup


def fil_url(x):
    cond = 'url' in x.get('href') and '/search' not in x.get('href')
    return cond


def lucky(query):
    url = f'https://www.google.com.br/search?q={query}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    urls = filter(fil_url, soup.select('div > a[href]'))
    urls = map(lambda y: y.get('href'), urls)
    urls = list(map(lambda z: z[z.index('=')+1:], urls))

    for index in urls:
        print(webbrowser.open(index))


if __name__ == "__main__":
    lucky(' '.join(sys.argv[1:]).strip())
