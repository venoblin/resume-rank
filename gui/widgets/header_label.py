from kivy.uix.label import Label

class HeaderLabel(Label):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

    self.bold = False
    self.font_size = 25