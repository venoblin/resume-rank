from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from gui.containers.window import Window
from gui.widgets.header_label import HeaderLabel

class ResumeManager(App):
    def build(self):
        self.title = "Resume Manager"
        window = Window()

        resumes = BoxLayout(orientation='vertical')
        resumes.add_widget(HeaderLabel(text='Resumes'))

        window.add_widget(resumes)

        return window