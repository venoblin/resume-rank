from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from gui.widgets.label import Label
from gui.widgets.header_label import HeaderLabel
from gui.widgets.file_chooser import FileChooser

class Resumes(BoxLayout):
  resumes = []
  file_chooser = None
  
  def __init__(self, resumes = []):
    super().__init__()
    self.orientation = 'vertical'
    self.resumes = resumes

    header = HeaderLabel(text='Resumes')

    resumes_container = GridLayout(cols=1)

    if len(resumes):
      for r in resumes:
        resume_label = Label(text=r['file_name'])
        resumes_container.add_widget(resume_label)
    else:
      resume_label = Label(text='No resumes uploaded!')
      resumes_container.add_widget(resume_label)
    
    file_chooser = FileChooser()

    self.add_widget(file_chooser)
    self.add_widget(header)
    self.add_widget(resumes_container)

    def _upload_file(self):
      pass