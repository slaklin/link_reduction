import os
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
import argparse


def shorten_link(token, link):
    auth_header = {"Authorization": token}
    response = requests.post("https://api-ssl.bitly.com/v4/shorten",
                             json={"long_url": link},
                             headers=auth_header)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, link):
    url = urlparse(link)
    auth_header = {"Authorization": token}
    bitlink = f'{url.netloc}{url.path}'
    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
        headers=auth_header)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, link):
    url = urlparse(link)
    auth_header = {"Authorization": token}
    url = f'{url.netloc}{url.path}'
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{url}",
                            headers=auth_header)
    return response.ok


def main():
    load_dotenv()
    bitly_access_token = os.getenv("BITLY_ACCESS_TOKEN")
    parser = argparse.ArgumentParser('Описание программы')
    parser.add_argument('link', help='Введите ссылку.')
    args = parser.parse_args()
    link = args.link
    try:
        if is_bitlink(bitly_access_token, link):
            print('Количество кликов:', count_clicks(bitly_access_token, link))
        else:
            print('Сокращенная ссылка:', shorten_link(bitly_access_token, link))
    except requests.exceptions.HTTPError:
        print('Вы ввели неправильную ссылку или неверный токен, попробуйте ещё раз.')


if __name__ == '__main__':
    main()
