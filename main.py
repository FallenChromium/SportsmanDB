from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from view.MainWindow import MainWindow
from controller.AppController import AppController

class App(MDApp):
    controller = ObjectProperty(None)
    def build(self):
        self.controller = AppController()
        return MainWindow()

App().run()