from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from gui.widgets.container import Container
from gui.widgets.containers.resumes import Resumes

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle('Resume Manager')

    window = Container()
    window.layout.addWidget(Resumes())

    self.setCentralWidget(window)
    
  
