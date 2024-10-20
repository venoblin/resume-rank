from PySide6.QtWidgets import QMainWindow, QStackedLayout
from gui.widgets.container import Container
from gui.widgets.containers.finder import Finder

class MainWindow(QMainWindow):
  stack: QStackedLayout
  
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle('Resume Manager')
    self.stack = QStackedLayout()

    self.stack.addWidget(Finder())
    self.stack.setCurrentIndex(0)
    
    self.setLayout(self.stack)
