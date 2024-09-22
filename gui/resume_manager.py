from kivy.app import App
from kivy.graphics import Color, Rectangle
from gui.containers.window import Window
from gui.containers.resumes import Resumes
from gui.containers.job_description import JobDescription
from core.files import Files

class ResumeManager(App):
    root = None
    
    def build(self):
        self.title = "Resume Manager"

        self.root = Window()
        self.root.bind(size=self._update_rect, pos=self._update_rect)
        
        resume_files = self.get_resumes()
        resumes = Resumes(resume_files)
        resumes.size_hint = (0.3, 1)

        job_desc = JobDescription()
        job_desc.size_hint = (0.7, 1)
        
        self.root.add_widget(job_desc)
        self.root.add_widget(resumes)

        with self.root.canvas.before:
            Color(31 / 255, 31 / 255, 31 / 255, 1)
            self.rect = Rectangle(size=self.root.size, pos=self.root.pos)

        return self.root
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def get_resumes(self):
        return Files('files/resumes').get_files()
