import requests
from concurrent.futures.thread import ThreadPoolExecutor

def make_request(url):
    req = requests.get(url)
    print(req.status_code)
    print(req.url)
    print()


def main():
    urls = [
        'https://www.youtube.com/watch?v=rZGi1SCj1fU&t=31s',
        'https://www.debian.org/',
        'https://docs.oracle.com/javase/tutorial/java/index.html'
    ]
    with ThreadPoolExecutor() as executor:
        executor.map(make_request, urls)


if __name__ == '__main__':
    main()
