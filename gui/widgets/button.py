from kivy.uix.button import Button as KivyButton
from gui.constants.sizes import Sizes

class Button(KivyButton):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.font_size = Sizes.FONT_SIZE_M
    self.size_hint = (None, None)
    self.size = (400, 100)
    self.background_color = (2 / 255, 103 / 255, 193 / 255, 1)