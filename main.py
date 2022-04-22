from kivymd.app import MDApp
from view.MainWindow import MainWindow

class App(MDApp):
    def build(self):
        return MainWindow()

App().run()