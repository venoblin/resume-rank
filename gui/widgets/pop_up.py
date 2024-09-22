from kivy.uix.popup import Popup as KivyPopUp

class PopUp(KivyPopUp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    