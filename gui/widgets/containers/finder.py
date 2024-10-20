from gui.widgets.container import Container
from gui.widgets.resumes import Resumes
from gui.widgets.job_description import JobDescription

class Finder(Container):
  def __init__(self, type='horizontal'):
    super().__init__(type)

    self.layout.addWidget(JobDescription())
    self.layout.addWidget(Resumes())

