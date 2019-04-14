from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from news_getter import NewsGetter

print(NewsGetter().news_text)

class MyApp(App):
    def build(self):
        main_layout = GridLayout(rows=2, cols=1)

        bottom_button = BoxLayout()
        bottom_button.add_widget(Button(text='News'))
        bottom_button.add_widget(Button(text='Chat'))
        bottom_button.add_widget(Button(text='Videos'))
        bottom_button.add_widget(Button(text='Books'))

        news_grid = GridLayout(rows=3, cols=3, padding=[15], spacing=[5, 5])
        for i in range(9):
            news_grid.add_widget(Button(text=str(i)))


        alc = AnchorLayout(anchor_x='center', anchor_y='top')
        alc.add_widget(news_grid)


        alb = AnchorLayout(anchor_x='center', anchor_y='bottom', size_hint=[.05, .05])
        alb.add_widget(bottom_button)


        main_layout.add_widget(alc)
        main_layout.add_widget(alb)
        return main_layout



if __name__ == '__main__':
    MyApp().run()