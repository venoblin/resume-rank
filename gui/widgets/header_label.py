from PySide6.QtWidgets import QLabel

class HeaderLabel(QLabel):
  def __init__(self, text=''):
    super(HeaderLabel, self).__init__()

    self.setText(text)

    font = self.font()
    font.setPointSize(30)
    font.setBold(True)

    self.setFont(font)
