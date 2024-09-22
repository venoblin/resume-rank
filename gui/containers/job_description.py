from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from gui.widgets.button import Button
from gui.widgets.header_label import HeaderLabel
from gui.constants.sizes import Sizes

class JobDescription(BoxLayout):
  def __init__(self):
    super().__init__()
    self.orientation = 'vertical'

    header = HeaderLabel(text='Job Description')

    job_desc_text = TextInput(multiline=True)
    job_desc_text.font_size = Sizes.FONT_SIZE_M
    job_desc_text.padding = 20
    find_resume_btn = Button(text='Find Best Resume')

    self.add_widget(header)
    self.add_widget(job_desc_text)
    self.add_widget(find_resume_btn)