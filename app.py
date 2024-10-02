from PySide6.QtWidgets import QApplication
from gui.windows.main_window import MainWindow
import sys

def main():
  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  app.exec()

if __name__ == '__main__':
  main()