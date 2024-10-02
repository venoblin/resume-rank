from PySide6.QtWidgets import QVBoxLayout, QWidget
from gui.widgets.header_label import HeaderLabel

class Resumes(QVBoxLayout):
  def __init__(self):
    super(Resumes, self).__init__()

    header = HeaderLabel(text='Resumes')

    self.addWidget(header)