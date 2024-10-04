from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel
from gui.widgets.button import Button

class JobDescription(Container):
  def __init__(self):
    super().__init__()

    header = HeaderLabel(text='Job Description')
    find_btn = Button(text='Find Best Resume')

    self.layout.addWidget(header)
    self.layout.addWidget(find_btn)