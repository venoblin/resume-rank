from kivy.app import App
from gui.widgets.window import Window

class ResumeManager(App):
    def build(self):
        self.title = "Resume Manager"
        window = Window()

        return window