from PySide6.QtWidgets import QStackedLayout
from gui.widgets.container import Container
from gui.widgets.containers.resumes import Resumes
from gui.widgets.button import Button
from gui.widgets.file_viewer import FileViewer

class ResumeChecker(Container):
  stack: QStackedLayout
  resumes_container: Resumes
  file_viewer: FileViewer
  
  def __init__(self, stack):
    super().__init__(type='vertical')
    self.stack = stack

    self.file_viewer = FileViewer()
    self.resumes_container = Resumes(is_checking=True)

    button = Button(text='Back')
    button.clicked.connect(self._back_handler)

    self.layout.addWidget(self.file_viewer)
    self.layout.addWidget(self.resumes_container)
    self.layout.addWidget(button)

  def _back_handler(self):
    self.stack.setCurrentIndex(0)

  def update_resumes(self, resumes):
    self.resumes_container.update_resumes(resumes)
    self.file_viewer.update_path(resumes[0]['file_path'])