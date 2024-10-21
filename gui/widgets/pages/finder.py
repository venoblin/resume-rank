from PySide6.QtWidgets import QStackedLayout
from gui.widgets.container import Container
from gui.widgets.containers.resumes import Resumes
from gui.widgets.containers.job_description import JobDescription

class Finder(Container):
  stack: QStackedLayout
  
  def __init__(self, stack):
    super().__init__(type='horizontal')
    self.stack = stack

    job_description = JobDescription(stack=self.stack)
    resumes = Resumes()

    self.layout.addWidget(job_description)
    self.layout.addWidget(resumes)

