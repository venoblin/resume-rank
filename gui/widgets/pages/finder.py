from PySide6.QtWidgets import QStackedLayout
from gui.widgets.container import Container
from gui.widgets.containers.resumes import Resumes
from gui.widgets.containers.job_description import JobDescription

class Finder(Container):
  stack: QStackedLayout
  
  def __init__(self, stack):
    super().__init__(type='horizontal')
    self.stack = stack

    self.layout.addWidget(JobDescription())
    self.layout.addWidget(Resumes())

