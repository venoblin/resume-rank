from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel

class Resumes(Container):
  def __init__(self):
    super(Resumes, self).__init__()

    header = HeaderLabel(text='Resumes')

    self.layout.addWidget(header)