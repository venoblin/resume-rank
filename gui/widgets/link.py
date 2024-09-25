from gui.widgets.button import Button

class Link(Button):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.size_hint = (None, None)
    self.background_color = (0, 0, 0, 0)