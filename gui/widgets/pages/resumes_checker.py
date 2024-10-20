from PySide6.QtWidgets import QStackedLayout
from gui.widgets.container import Container
from gui.widgets.containers.resumes import Resumes

class ResumeChecker(Container):
  stack: QStackedLayout
  
  def __init__(self, stack):
    super().__init__(type='horizontal')
    self.stack = stack

    self.layout.addWidget(Resumes(is_checking=True))