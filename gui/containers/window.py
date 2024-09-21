from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from gui.widgets.header_label import HeaderLabel

class Window(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'

        with self.canvas.before:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        