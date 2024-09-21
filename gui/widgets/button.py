from kivy.uix.button import Button as KivyButton

class Button(KivyButton):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.size_hint = (0.5, 0.2)