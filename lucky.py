import sys
import webbrowser
from googlesearch import search


def lucky(query):
    urls = search(query, lang='pt-br', stop=5)
    for url in urls:
        webbrowser.open(url)


if __name__ == "__main__":
    lucky(' '.join(sys.argv[1:]).strip())
