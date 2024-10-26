from PySide6.QtWidgets import QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6 import QtCore 
from gui.widgets.container import Container

class FileViewer(QWidget):
    web_view: QWebEngineView
    
    def __init__(self, file_path = ''):
        super().__init__()

        self.webview = QWebEngineView()
        self.webview.setUrl(QtCore.QUrl.fromLocalFile(file_path))

        viewer = Container()
        viewer.layout.addWidget(self.webview)

        self.setLayout(viewer.layout)
    
    def update_path(self, new_path):
        self.web_view.setUrl(QtCore.QUrl.fromLocalFile(new_path))