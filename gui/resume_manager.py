from kivy.app import App
from gui.containers.window import Window
from gui.containers.resumes import Resumes
from gui.containers.job_description import JobDescription

class ResumeManager(App):
    def build(self):
        self.title = "Resume Manager"
        window = Window()
        resumes = Resumes(['resume1', 'resume2', 'resume3'])
        resumes.size_hint = (0.3, 1)
        job_desc = JobDescription()
        job_desc.size_hint = (0.7, 1)
        
        window.add_widget(job_desc)
        window.add_widget(resumes)

        return window
