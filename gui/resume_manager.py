from kivy.app import App
from kivy.graphics import Color, Rectangle
from gui.containers.window import Window
from gui.containers.resumes import Resumes
from gui.containers.job_description import JobDescription

class ResumeManager(App):
    def build(self):
        self.title = "Resume Manager"

        root = Window()
        root.bind(size=self._update_rect, pos=self._update_rect)

        resumes = Resumes(['resume1', 'resume2', 'resume3'])
        resumes.size_hint = (0.3, 1)

        job_desc = JobDescription()
        job_desc.size_hint = (0.7, 1)
        
        root.add_widget(job_desc)
        root.add_widget(resumes)

        with root.canvas.before:
            Color(31 / 255, 31 / 255, 31 / 255, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)

        return root
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
