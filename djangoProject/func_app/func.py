import requests
from bs4 import BeautifulSoup
import csv

#CSV = 'chanel.csv'

HOST = 'https://rumble.com/'
URL = 'https://rumble.com/account/channel/subscriptions'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'cookie':'_ga=GA1.2.346463566.1670242121; _gid=GA1.2.696958826.1670242121; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; u_s=VVgCQO646nhbkIELesn; PHPSESSID=gma7bh252ijnrd63b8r5tuflqs617en1; _gat_rumble=1'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    get_content(r.text)
    return


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    itemsGrid = soup.select('.table-grid')[0] #получаю первую таблицу string html
    items = itemsGrid.select('tr')

    items.pop(0) #удаляю первую строку в таблице

    chanel = []
    for i in range(len(items)):
        chanel.append({
            'title': items[i].select('span')[0].text,
            'subscribe':items[i].select('span')[1].text,
        })

    return chanel


#html = get_html(URL)


# def save_doc(items, path):
#     with open(path, 'w', newline='', encoding="utf-8-sig") as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(['Название Канала', 'Количество подписчиков'])
#         for item in items:
#             writer.writerow([item['title'], item['subscribe']])