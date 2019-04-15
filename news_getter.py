import urllib.request
from bs4 import BeautifulSoup
import webbrowser

class NewsGetter():
    def __init__(self, **kwargs):
        self.page = urllib.request.urlopen('https://www.foxbusiness.com/category/opinion')
        self.news_text = []


    def get_news(self):

        soup = BeautifulSoup(self.page, features="lxml")
        elems = soup.select("div.info h3 a", limit=9)
        for i in range(len(elems)):
            self.news_text.append(elems[i].get_text())

        print(self.news_text)
        #print(news_hrefs)

        with open('news.txt', 'w') as f:
            f.write(str(self.news_text))


    def get_href(self):
        news_hrefs = []
        aTeg = []
        soup = BeautifulSoup(self.page, features="lxml")
        elems = soup.select("div.info h3 a", limit=9)
        for i in range(len(elems)):
            aTeg.append(elems[i].get_text())
            news_hrefs.append(elems[i].attrs["href"])

        with open('hrefs.txt', 'w') as f:
            f.write(str(news_hrefs))

        print(aTeg)
        #print(news_hrefs)
        return news_hrefs



    def open_browser(self, href):
        webbrowser.open_new_tab(href)
