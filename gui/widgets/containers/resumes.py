from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel
from gui.widgets.button import Button

class Resumes(Container):
  def __init__(self):
    super(Resumes, self).__init__()

    header = HeaderLabel(text='Resumes')
    upload_resume_btn = Button(text='Upload Resume')

    self.layout.addWidget(header)
    self.layout.addWidget(upload_resume_btn)