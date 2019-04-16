from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from news_getter import NewsGetter
import webbrowser

hrefs = NewsGetter()
hrefs.get_href()
hrefs.correct_href_maker()

class MyApp(App):

    def build(self):
        main_layout = GridLayout(rows=2, cols=1)

        bottom_button = BoxLayout()
        bottom_button.add_widget(Button(text='News'))
        bottom_button.add_widget(Button(text='Chat'))
        bottom_button.add_widget(Button(text='Videos'))
        bottom_button.add_widget(Button(text='Books'))

        news_grid = GridLayout(rows=3, cols=3, padding=[15], spacing=[5, 5])
        buttons = []
        for i in range(9):
            NG = NewsGetter()
            NG.get_news()
            buttons.append(Button(text=NG.news_text[i]))
            if i == 0:
                buttons[i].bind(on_press=hrefs.open_browser0)
            elif i == 1:
                buttons[i].bind(on_press=hrefs.open_browser1)
            elif i == 2:
                buttons[i].bind(on_press=hrefs.open_browser2)
            elif i == 3:
                buttons[i].bind(on_press=hrefs.open_browser3)
            elif i == 4:
                buttons[i].bind(on_press=hrefs.open_browser4)
            elif i == 5:
                buttons[i].bind(on_press=hrefs.open_browser5)
            elif i == 6:
                buttons[i].bind(on_press=hrefs.open_browser6)
            elif i == 7:
                buttons[i].bind(on_press=hrefs.open_browser7)
            elif i == 8:
                buttons[i].bind(on_press=hrefs.open_browser8)
            else:
                buttons[i].bind(on_press=hrefs.open_browser9)

            news_grid.add_widget(buttons[i])


        alc = AnchorLayout(anchor_x='center', anchor_y='top')
        alc.add_widget(news_grid)


        alb = AnchorLayout(anchor_x='center', anchor_y='bottom', size_hint=[.05, .05])
        alb.add_widget(bottom_button)


        main_layout.add_widget(alc)
        main_layout.add_widget(alb)
        return main_layout



if __name__ == '__main__':
    MyApp().run()
