import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()

with open('newFile.txt', 'wb') as file:
    for chunk in response.iter_content(100000):
        file.write(chunk)
