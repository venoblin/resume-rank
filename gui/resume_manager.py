from PySide6.QtWidgets import QApplication, QWidget
import sys

class ResumeManager():
  app: QApplication
  
  def __init__(self):
    self.app = QApplication(sys.argv)

    window = QWidget()
    window.show()

  def run(self):
    self.app.exec()