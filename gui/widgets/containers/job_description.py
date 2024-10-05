from PySide6.QtWidgets import QPlainTextEdit
from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel
from gui.widgets.button import Button

class JobDescription(Container):
  def __init__(self):
    super().__init__()

    header = HeaderLabel(text='Job Description')
    textarea = QPlainTextEdit()
    textarea.setPlaceholderText('Past job description here...')
    find_btn = Button(text='Find Best Resume')

    self.layout.addWidget(header)
    self.layout.addWidget(textarea)
    self.layout.addWidget(find_btn)