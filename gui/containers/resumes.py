from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from gui.widgets.label import Label
from gui.widgets.button import Button
from gui.widgets.header_label import HeaderLabel

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

    self.file_chooser = FileChooserListView()
    popup = Popup(
      title = 'Upload Resume',
      content = self.file_chooser
    )

    resume_upload_btn = Button(text='Upload Resume')
    
    self.add_widget(header)
    self.add_widget(resumes_container)
    self.add_widget(resume_upload_btn)
    self.add_widget(popup)

    def _upload_file(self):
      pass