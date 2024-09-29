from PySide6.QtWidgets import QLabel

class HeaderLabel(QLabel):
  def __init__(self, label = ''):
    super(HeaderLabel, self).__init__()

    self.setText(label)

    font = self.font()
    font.setPointSize(50)
    font.setBold(True)

    self.setFont(font)
