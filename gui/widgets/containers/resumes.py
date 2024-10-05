from PySide6.QtWidgets import QFileDialog
from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel
from gui.widgets.button import Button

class Resumes(Container):
  def __init__(self):
    super().__init__()

    header = HeaderLabel(text='Resumes')
    open_dialog_btn = Button(text='Upload Resume')
    open_dialog_btn.clicked.connect(self.open_dialog)

    self.layout.addWidget(header)
    self.layout.addWidget(open_dialog_btn)

  def open_dialog(self):
    file_name = QFileDialog.getOpenFileName(self, 'Select Resume', '', 'Resume Files (*.pdf)')

    if file_name:
      print(file_name)