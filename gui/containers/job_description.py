from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class JobDescription(BoxLayout):
  def __init__(self):
    super().__init__()
    self.orientation = 'vertical'

    job_desc_text = TextInput(multiline=True)
    find_resume_btn = Button(text='Find Best Resume')

    self.add_widget(job_desc_text)
    self.add_widget(find_resume_btn)