import requests
from bs4 import BeautifulSoup
import json

def save_articles(article_list):
    with open('articles.json', 'w') as outfile:
        json.dump(article_list, outfile)

def scrape_news():
    article_list = []
    try:
        response = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(response.content, 'xml')
        articles = soup.find_all('item')
        for article in articles:
            title = article.find('title').text.strip()
            link = article.find('link').text.strip()
            published = article.find('pubDate').text.strip()
            article_dict = {
                'title': title,
                'link': link,
                'published': published
            }
            article_list.append(article_dict)
        save_articles(article_list)
    except Exception as e:
        print("Error: {}".format(str(e)))

scrape_news()
