from kivy.app import App
from .view import MainWindow
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        return MainWindow()

