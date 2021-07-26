# определяем список хабов, которые нам интересны
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

import requests
from bs4 import BeautifulSoup

url_habr = 'https://habr.com'
# получаем страницу с самыми свежими постами
ret = requests.get(url_habr + '/ru/all/')
soup = BeautifulSoup(ret.text, 'html.parser')

# извлекаем посты
posts = soup.find_all('article', class_='tm-articles-list__item')
for post in posts:

    post_id = post.get('id')
    # если идентификатор не найден, это что-то странное, пропускаем
    if not post_id:
        continue
    hub_lower = post.text.lower()
    if set(KEYWORDS) & set(hub_lower.split()):
        times = post.find('time')
        title_time = times.get('title')
        print('date', title_time)

        article = post.find('a', class_='tm-article-snippet__title-link')
        title_article = article.span.get_text()
        print('title', title_article)

        print('article', url_habr + article.get('href'))

        print()
