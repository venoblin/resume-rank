from kivy.uix.filechooser import FileChooser as KivyFileChooser

class FileChooser(KivyFileChooser):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)