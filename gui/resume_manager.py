from kivy.app import App
from gui.window import Window

class ResumeManager(App):
    def build(self):
        self.title = "Resume Manager"
        return Window()