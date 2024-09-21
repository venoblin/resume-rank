from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from gui.containers.window import Window
from gui.widgets.header_label import HeaderLabel

class ResumeManager(App):
    def build(self):
        self.title = "Resume Manager"
        window = Window()

        job_description = BoxLayout(orientation='vertical')
        job_description_text = TextInput(multiline=True)
        job_description.add_widget(job_description_text)

        resumes = BoxLayout(orientation='vertical')
        resume_upload_btn = Button(text='Upload Resume')
        resumes.add_widget(HeaderLabel(text='Resumes'))
        resumes.add_widget(resume_upload_btn)
        
        window.add_widget(job_description)
        window.add_widget(resumes)

        return window