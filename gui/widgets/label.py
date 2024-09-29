from PySide6.QtWidgets import QLabel

class Label(QLabel):
  def __init__(self, label = ''):
    super(Label, self).__init__()

    self.setText(label)

    font = self.font()
    font.setPointSize(10)

    self.setFont(font)