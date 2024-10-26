from PySide6.QtWidgets import QStackedLayout
from gui.widgets.container import Container
from gui.widgets.containers.resumes import Resumes
from gui.widgets.button import Button

class ResumeChecker(Container):
  stack: QStackedLayout
  resumes_container: Resumes
  
  def __init__(self, stack):
    super().__init__(type='vertical')
    self.stack = stack

    self.resumes_container = Resumes(is_checking=True)

    button = Button(text='Back')
    button.clicked.connect(self._back_handler)

    self.layout.addWidget(self.resumes_container)
    self.layout.addWidget(button)

  def _back_handler(self):
    self.stack.setCurrentIndex(0)

  def update_resumes(self, resumes):
    self.resumes_container.update_resumes(resumes)