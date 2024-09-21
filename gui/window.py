from kivy.uix.boxlayout import BoxLayout

class Window(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.orientation = 'vertical'

        resume_layout = BoxLayout(orientation='vertical')
        