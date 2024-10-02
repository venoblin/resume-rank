from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from gui.widgets.containers.resumes import Resumes

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle('Resume Manager')

    layout = QVBoxLayout()
    layout.addWidget(Resumes())

    window = QWidget()
    window.setLayout(layout)
    self.setCentralWidget(window)
    
  
