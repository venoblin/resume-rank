from PySide6.QtWidgets import QStackedLayout
from gui.widgets.container import Container
from gui.widgets.containers.resumes import Resumes
from gui.widgets.button import Button

class ResumeChecker(Container):
  stack: QStackedLayout
  resumes = []
  
  def __init__(self, stack):
    super().__init__(type='vertical')
    self.stack = stack

    resumes_container = Resumes(resumes=self.resumes, is_checking=True)

    button = Button(text='Back')
    button.clicked.connect(self._back_handler)

    self.layout.addWidget(resumes_container)
    self.layout.addWidget(button)

  def _back_handler(self):
    self.stack.setCurrentIndex(0)