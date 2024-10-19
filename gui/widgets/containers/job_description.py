from PySide6.QtWidgets import QPlainTextEdit
from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel
from gui.widgets.button import Button
from core.files import Files

class JobDescription(Container):
  textarea: QPlainTextEdit
  
  def __init__(self):
    super().__init__()

    header = HeaderLabel(text='Job Description')
    self.textarea = QPlainTextEdit()
    self.textarea.setPlaceholderText('Paste job description here...')
    find_btn = Button(text='Find Best Resume')
    find_btn.clicked.connect(self._find_resume_handler)

    self.layout.addWidget(header)
    self.layout.addWidget(self.textarea)
    self.layout.addWidget(find_btn)

  def _find_resume_handler(self):
    content = self.textarea.toPlainText()
    resumes = Files('files/resumes').get_files()
