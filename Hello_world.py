import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
####### root ###########
class TheRoot(FloatLayout):
    def __init__(self, **kwargs):
        super(TheRoot, self).__init__(**kwargs)
        self.add_widget(Label(text="Hello world"))
####### App #############
class Hello(App):
    def build(self):
        return TheRoot()
Hello().run()