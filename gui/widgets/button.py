from PySide6.QtWidgets import QPushButton

class Button(QPushButton):
  def __init__(self, text=''):
    super().__init__(text)