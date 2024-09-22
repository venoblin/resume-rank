from kivy.uix.label import Label
from gui.constants.sizes import Sizes

class HeaderLabel(Label):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

    self.bold = True
    self.font_size = Sizes.FONT_SIZE_LG
    self.size_hint = (1, None)
    self.size = (0, 150)