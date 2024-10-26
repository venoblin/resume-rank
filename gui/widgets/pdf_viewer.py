from PySide6.QtWidgets import QWidget, QWebEngineView
from gui.widgets.container import Container

class PDFViewer(QWidget):
    def __init__(self, pdf_path):
        super().__init__()

        webview = QWebEngineView()
        webview.setUrl(pdf_path)

        viewer = Container()
        viewer.addWidget(self.webview)