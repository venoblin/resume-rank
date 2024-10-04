from PySide6.QtWidgets import QMainWindow
from gui.widgets.container import Container
from gui.widgets.containers.resumes import Resumes
from gui.widgets.containers.job_description import JobDescription

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle('Resume Manager')

    window = Container(type='horizontal')
    window.layout.addWidget(JobDescription())
    window.layout.addWidget(Resumes())

    self.setCentralWidget(window)
    
  
