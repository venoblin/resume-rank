from kivy.uix.label import Label as KivyLabel
from gui.constants.sizes import Sizes

class Label(KivyLabel):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.font_size = Sizes.FONT_SIZE_M