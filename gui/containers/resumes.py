from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from gui.widgets.header_label import HeaderLabel

class Resumes(BoxLayout):
  def __init__(self):
    super().__init__()
    self.orientation = 'vertical'

    resume_upload_btn = Button(text='Upload Resume')
    
    self.add_widget(HeaderLabel(text='Resumes'))
    self.add_widget(resume_upload_btn)