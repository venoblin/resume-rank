from kivy.uix.filechooser import FileChooserListLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from gui.widgets.button import Button

class FileChooser(Popup):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    wrapper = BoxLayout(orientation='vertical')
    file_chooser = FileChooserListLayout()
    close_btn = Button(text='Cancel')
    close_btn.bind(on_press=self.dismiss)

    wrapper.add_widget(file_chooser)
    wrapper.add_widget(close_btn)

    self.title = 'Upload Resume'
    self.content = wrapper
    self.size_hint = (None, None)
    self.size = (400, 400)