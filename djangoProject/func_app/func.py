import re
import urllib

from bs4 import BeautifulSoup
import json
import requests
import urllib.request


def get_content(urlpath):
    headers = {'User-agents': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/108.0.0.0 Safari/537.36'}

    url = "http://www.youtube.com/" + urlpath + "/channels"
    urllib.request.urlretrieve(url, 'test.html')
    f = open('test.html', 'r', encoding='utf-8')  # открываю файл для чтения
    f = f.read()  # читаю файл и записываю в переменную f
    soup = BeautifulSoup(f,
                         features="lxml")  # конвертирую текст прочитанный из файла в lxml и записываю в переменную soap
    script = soup.select("script")  # ищу в html тэг скрипт
    for scriptTag in script:  # в цикле перебираю все найденные тэги скрипт
        result = scriptTag.getText()  # получаю текст из тэга скрипт
        if result:  # если текст найден
            result = result.find("var ytInitialData = ")  # ищу в тексте var ytInitialData
            if result != -1 and not (result is None):  # если такой текст найден
                result = re.sub("var ytInitialData = ", '',
                                scriptTag.getText())  # удаляю из найденного текста поисковый текст
                result = \
                    json.loads(result[:-1])["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][4]["tabRenderer"][
                        "content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0][
                        "gridRenderer"]["items"]  # перевожу текст в json формат и ищу по ключам массив с подписками
                result = [
                    canal['gridChannelRenderer']["title"]['simpleText'] if 'gridChannelRenderer' in canal else None for
                    canal in result]  # конвертирую найденные названаия подписки из объектов
                return result


#print(get_content())
