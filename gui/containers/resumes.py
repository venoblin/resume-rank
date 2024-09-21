from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from gui.widgets.header_label import HeaderLabel

class Resumes(BoxLayout):
  def __init__(self, resumes = []):
    super().__init__()
    self.orientation = 'vertical'

    header = HeaderLabel(text='Resumes')

    resumes_container = BoxLayout(orientation='vertical')

    if len(resumes):
      for r in resumes:
        resume_label = Label(text=r)
        resumes_container.add_widget(resume_label)
    else:
      resume_label = Label(text='No resumes uploaded!')
      resumes_container.add_widget(resume_label)

    resume_upload_btn = Button(text='Upload Resume')
    
    self.add_widget(header)
    self.add_widget(resumes_container)
    self.add_widget(resume_upload_btn)