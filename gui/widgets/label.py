from PySide6.QtWidgets import QLabel

class Label(QLabel):
  
  def __init__(self, text=''):
    super(Label, self).__init__()

    self.setText(text)

    font = self.font()
    font.setPointSize(10)

    self.setFont(font)