import requests
import bs4
from pprint import pprint

KEYS_WORDS = ['IT-компании', 'Python *', 'Удалённая работа']
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}


url = 'https://habr.com/ru/all/'
response = requests.get(url=url, headers=HEADERS)
pprint(response.raise_for_status())
answer = response.text
soup = bs4.BeautifulSoup(answer, features='html.parser')
articles = soup.findAll('article')
for article in articles:
    hubs = article.findAll(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        if hub in KEYS_WORDS:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            name = article.find('h2').find('span').text
            # time = article.find(class_='tm-article-snippet__datetime-published').text
            time = article.find('time')['title']
            result = f'{time} Статья - {name} - {url}{href}'
            pprint(result)

