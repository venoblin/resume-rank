from gui.widgets.container import Container
from gui.widgets.label import Label
from gui.widgets.button import Button

class Resume(Container):
  def __init__(self, resume):
    super().__init__(type='horizontal')
    
    label = Label(text=resume['file_name'])
    delete_btn = Button(text='Delete')

    self.layout.addWidget(label)
    self.layout.addWidget(delete_btn)
