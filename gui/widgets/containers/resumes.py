from PySide6.QtWidgets import QFileDialog
from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel
from gui.widgets.button import Button
from gui.widgets.label import Label
from core.directory import Directory
from core.utils import run_command

class Resumes(Container):
  is_checking: bool
  resume_container: Container
  resumes: list
  
  def __init__(self, resumes = [], is_checking = False):
    super().__init__()
    header = HeaderLabel(text='Resumes')
    self.is_checking = is_checking
    if len(resumes) == 0:
      self.resumes = Directory('files/resumes').get_files()
    else:
      self.resumes = resumes

    self.resume_container = Container()
    self._create_resume_widgets()

    self.layout.addWidget(header)
    self.layout.addWidget(self.resume_container)
    if not self.is_checking:
      open_dialog_btn = Button(text='Upload Resume')
      open_dialog_btn.clicked.connect(self.open_dialog)
      self.layout.addWidget(open_dialog_btn)

  def open_dialog(self):
    file = QFileDialog.getOpenFileName(self, 'Upload Resume', '', 'Resume Files (*.pdf)')

    if file[0]:
      run_command(f'cp {file[0]} ./files/resumes')
      self._refresh_resumes()

  def _refresh_resumes(self):
    self.resume_container.clear_layout()
    self._create_resume_widgets()
  
  def _delete_resume(self, resume):
    run_command(f'rm files/${resume['file_path']}')
    self._refresh_resumes()
  
  def _create_resume_widgets(self):
    if self.resumes:
      for r in self.resumes:
        resume = Container(type='horizontal')
        label = Label(text=r['file_name'])

        resume.layout.addWidget(label)
        if not self.is_checking:
          delete_btn = Button(text='Delete')
          delete_btn.clicked.connect(lambda: self._delete_resume(r))
          resume.layout.addWidget(delete_btn)
        
        self.resume_container.layout.addWidget(resume)
    else:
      self.resume_container.layout.addWidget(Label('No resumes!'))


