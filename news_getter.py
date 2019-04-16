import urllib.request
from bs4 import BeautifulSoup
import webbrowser

class NewsGetter():
    def __init__(self, **kwargs):
        self.page = urllib.request.urlopen('https://www.foxbusiness.com/category/opinion')
        self.news_text = []
        self.news_hrefs = []


    def get_news(self):

        soup = BeautifulSoup(self.page, features="lxml")
        elems = soup.select("div.info h3 a", limit=9)
        for i in range(len(elems)):
            self.news_text.append(elems[i].get_text())

        #print(self.news_text)

        with open('news.txt', 'w') as f:
            f.write(str(self.news_text))


    def get_href(self):
        soup = BeautifulSoup(self.page, features="lxml")
        elems = soup.select("div.info h3 a", limit=9)
        for i in range(len(elems)):
            self.news_hrefs.append(elems[i].attrs["href"])

        with open('hrefs.txt', 'w') as f:
            f.write(str(self.news_hrefs))

        #print(self.news_hrefs)

    def correct_href_maker(self):
        for i, world in enumerate(self.news_hrefs):
            if self.news_hrefs[i][0] != 'h' and self.news_hrefs[i][5] != ':':
                self.news_hrefs[i] = 'https://www.foxbusiness.com' + self.news_hrefs[i]


    def open_browser0(self, event):
        webbrowser.open_new_tab(self.news_hrefs[0])

    def open_browser1(self, event):
        webbrowser.open_new_tab(self.news_hrefs[1])

    def open_browser2(self, event):
        webbrowser.open_new_tab(self.news_hrefs[2])

    def open_browser3(self, event):
        webbrowser.open_new_tab(self.news_hrefs[3])

    def open_browser4(self, event):
        webbrowser.open_new_tab(self.news_hrefs[4])

    def open_browser5(self, event):
        webbrowser.open_new_tab(self.news_hrefs[5])

    def open_browser6(self, event):
        webbrowser.open_new_tab(self.news_hrefs[6])

    def open_browser7(self, event):
        webbrowser.open_new_tab(self.news_hrefs[7])

    def open_browser8(self, event):
        webbrowser.open_new_tab(self.news_hrefs[8])

    def open_browser9(self, event):
        webbrowser.open_new_tab(self.news_hrefs[9])

a = NewsGetter()
a.get_href()
a.correct_href_maker()
print(a.news_hrefs)
