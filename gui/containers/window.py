from kivy.uix.boxlayout import BoxLayout

class Window(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'horizontal'
        self.padding = (20, 40)