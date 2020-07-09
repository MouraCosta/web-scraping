import requests


def main():
    request = requests.get('https://github.com/timeline.json')
    timeline_dict = request.json()

    print(timeline_dict)


if __name__ == '__main__':
    main()
