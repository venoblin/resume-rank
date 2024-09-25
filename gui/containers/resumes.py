from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from gui.widgets.label import Label
from gui.widgets.header_label import HeaderLabel
from gui.widgets.file_chooser import FileChooser
from gui.widgets.button import Button

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

    open_file_chooser_btn = Button(text='Upload Resume')
    open_file_chooser_btn.bind(on_press=self._open_file_chooser)
    
    self.add_widget(header)
    self.add_widget(resumes_container)
    self.add_widget(open_file_chooser_btn)

  def _open_file_chooser(self, instance):
    file_chooser = FileChooser()
    file_chooser.open()