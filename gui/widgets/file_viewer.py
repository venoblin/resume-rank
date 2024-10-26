from PySide6.QtWidgets import QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from gui.widgets.container import Container

class FileViewer(QWidget):
    file_path: str
    
    def __init__(self, file_path = ''):
        super().__init__()
        self.file_path = file_path

        webview = QWebEngineView()
        webview.setUrl(self.file_path)

        viewer = Container()
        viewer.layout.addWidget(webview)