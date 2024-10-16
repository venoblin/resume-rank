from gui.widgets.container import Container
from gui.widgets.label import Label
from gui.widgets.button import Button
from core.utils import run_command

class Resume(Container):
  resume: dict
  
  def __init__(self, resume):
    super().__init__(type='horizontal')
    self.resume = resume

    label = Label(text=self.resume['file_name'])
    delete_btn = Button(text='Delete')
    delete_btn.clicked.connect(self._delete_handler)

    self.layout.addWidget(label)
    self.layout.addWidget(delete_btn)

  def _delete_handler(self):
    run_command(f'rm files/${self.resume['file_path']}')
