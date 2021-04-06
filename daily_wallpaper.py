#!/usr/bin/env python3

__author__ = "Trikzon"
__date__ = "2021-04-06"
__license__ = "MIT"
__copyright__ = "Copyright © 2021 Trikzon"

import os
from datetime import date
import platform

import praw  # TODO: Update praw
import requests
import tqdm
from bs4 import BeautifulSoup


def get_top_image(subreddit):
    reddit = praw.Reddit(user_agent="Trikzon")

    for submission in reddit.get_subreddit(subreddit, fetch=True).get_top_from_day():
        return submission


def get_image_url(submission: praw.objects.Subreddit):
    url = submission.url
    img_ext = ('jpg', 'jpeg', 'png', 'gif')

    if url.endswith(img_ext):
        return url
    elif 'imgur' in url and ('/a/' in url or '/gallery/' in url):
        r = requests.get(url).text
        soup_object = BeautifulSoup(r, 'html.parser')
        for link in soup_object.find_all('div', {'class': 'post-image'}):
            partial_url = link.img.get('src')
            # img_link comes as //imgur.com/id make it
            # https://imgur.com/id
            url = 'https:' + partial_url
            return url
    else:
        raw_url = url + '.jpg'
        try:
            r = requests.get(raw_url)
            r.raise_for_status()
            extension = r.headers['content-type'].split('/')[-1]
        except Exception as e:
            extension = ''

        if extension in img_ext:
            link = '{url}.{ext}'.format(url=url, ext=extension)
            return link


def download_image(url):
    path = os.path.join(os.path.dirname(__file__), "wallpapers")

    os.makedirs(path, exist_ok=True)

    today = str(date.today())
    _, extension = os.path.splitext(url)
    file_name = today + extension

    file_path = os.path.join(path, file_name)

    if os.path.exists(file_path):
        print(f"Re-downloading today's wallpaper to {file_path}.")
    else:
        print(f"Downloading today's wallpaper to {file_path}.")

    r = requests.get(url, stream=True)
    with open(file_path, 'wb') as outfile:
        for chunk in (
                tqdm.tqdm(
                    r.iter_content(chunk_size=1024),
                    total=(int(r.headers.get('content-length', 0)) // 1024),
                    unit='KB'
                )
        ):
            if chunk:
                outfile.write(chunk)
            else:
                return
    return file_path


def set_wallpaper(image_path):
    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    else:
        print(f"Unsupported platform: {platform.system()}")


def main():
    top_image = get_top_image("wallpaper")
    url = get_image_url(top_image)
    image_path = download_image(url)

    if image_path is None:
        print("Failed to set wallpaper.")
    else:
        set_wallpaper(image_path)


if __name__ == "__main__":
    main()
