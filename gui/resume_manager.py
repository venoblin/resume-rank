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

        job_desc = BoxLayout(orientation='vertical')
        job_desc_text = TextInput(multiline=True)
        find_resume_btn = Button(text='Find Best Resume')
        job_desc.add_widget(job_desc_text)
        job_desc.add_widget(find_resume_btn)

        resumes = BoxLayout(orientation='vertical')
        resume_upload_btn = Button(text='Upload Resume')
        resumes.add_widget(HeaderLabel(text='Resumes'))
        resumes.add_widget(resume_upload_btn)
        
        window.add_widget(job_desc)
        window.add_widget(resumes)

        return window