import requests
import string
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'apple'}

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise RuntimeError('Ошибка загрузки')

html_text = response.text
soup = BeautifulSoup(html_text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    description = article.find('div', class_="post__text").text.split()
    description = {d.strip(string.punctuation).lower() for d in description}
    if description & KEYWORDS:
        date = article.find('span', class_="post__time").text.strip()
        title = article.find('h2', class_="post__title").text.strip()
        link = article.find('a', class_="post__title_link").get('href')
        output_info = [date, title, link]
        print(output_info)
