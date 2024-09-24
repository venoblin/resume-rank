from kivy.uix.filechooser import FileChooserListLayout
from kivy.uix.popup import Popup

class FileChooser(Popup):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    file_chooser = FileChooserListLayout()
    self.title = 'Upload Resume'
    self.content = file_chooser