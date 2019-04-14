import urllib.request
from bs4 import BeautifulSoup


class NewsGetter():
    def __init__(self):
        self.news_text = []


    def get_news(self):
        page = urllib.request.urlopen('https://www.foxbusiness.com/category/opinion')

        soup = BeautifulSoup(page, 'html.parser')

        name_box = soup.find_all('div', class_='info')

        for i in range(len(name_box)):
            self.news_text.append(name_box[i].get_text())

        with open('news.txt', 'w') as f:
            f.write(str(self.news_text))

