from kivy.app import App
from gui.containers.window import Window
from gui.containers.resumes import Resumes
from gui.containers.job_description import JobDescription

class ResumeManager(App):
    def build(self):
        self.title = "Resume Manager"
        window = Window()
        resumes = Resumes()
        job_desc = JobDescription()
        
        window.add_widget(job_desc)
        window.add_widget(resumes)

        return window