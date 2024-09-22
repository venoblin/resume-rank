from kivy.uix.button import Button as KivyButton
from gui.constants.sizes import Sizes

class Button(KivyButton):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.font_size = Sizes.FONT_SIZE_M
    self.size_hint = (0.5, 0.2)
    self.background_color = (0, 1, 0, 1)