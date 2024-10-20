from PySide6.QtWidgets import QWidget, QStackedLayout
from gui.widgets.containers.finder import Finder

class MainWindow(QWidget):
  stack: QStackedLayout
  
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle('Resume Manager')
    self.stack = QStackedLayout()

    self.stack.addWidget(Finder())
    
    self.setLayout(self.stack)
