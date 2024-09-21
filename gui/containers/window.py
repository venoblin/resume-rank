from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from gui.widgets.header_label import HeaderLabel

class Window(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'horizontal'