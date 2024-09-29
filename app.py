from PySide6.QtWidgets import QApplication
from gui.windows.main_window import MainWindow
from gui.widgets.label import Label
import sys

def main():
  app = QApplication(sys.argv)

  window = MainWindow()
  window.setCentralWidget(Label('HEADER'))
  window.show()

  app.exec()

if __name__ == '__main__':
  main()