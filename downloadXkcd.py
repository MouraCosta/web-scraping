#!usr/bin/python3

import concurrent.futures.thread
import os

import requests
from bs4 import BeautifulSoup

if "Data" not in os.listdir(os.curdir):
    os.mkdir("Data/")
    os.chdir("./Data")
else:
    os.chdir("./Data")


def download_image(img_id):
    main_url = f"https://xkcd.com/{img_id}/"
    req = requests.get(main_url)
    soup = BeautifulSoup(req.text, "html.parser")

    # Getting the image url and download it
    image_url = "https:"+soup.select("div[id=comic] img[src]")[0].get("src")
    img = requests.get(image_url).content
    with open(f"tirinha{img_id}.png", "wb") as img_file:
        img_file.write(img)


img_id_list = (i for i in range(1, 500))
with concurrent.futures.thread.ThreadPoolExecutor() as executor:
    for id_ in img_id_list:
        executor.submit(download_image, id_)
print("done")
