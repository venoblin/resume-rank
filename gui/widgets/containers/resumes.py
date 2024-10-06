from PySide6.QtWidgets import QFileDialog
from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel
from gui.widgets.label import Label
from gui.widgets.button import Button
from core.files import Files
from core.utils import run_command

class Resumes(Container):
  resumes = []
  
  def __init__(self):
    super().__init__()
    self.resumes = self._get_resumes()

    header = HeaderLabel(text='Resumes')

    resume_container = Container()
    if self.resumes:
      for r in self.resumes:
        resume_container.layout.addWidget(Label(r['file_name']))
    else:
      resume_container.layout.addWidget(Label('No resumes!'))

    open_dialog_btn = Button(text='Upload Resume')
    open_dialog_btn.clicked.connect(self.open_dialog)

    self.layout.addWidget(header)
    self.layout.addWidget(resume_container)
    self.layout.addWidget(open_dialog_btn)

  def open_dialog(self):
    file = QFileDialog.getOpenFileName(self, 'Upload Resume', '', 'Resume Files (*.pdf)')

    if file:
      run_command(f'cp {file[0]} ./files/resumes')

  def _get_resumes(self):
    return Files('files/resumes').get_files()