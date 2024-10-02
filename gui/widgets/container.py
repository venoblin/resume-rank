from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QWidget

class Container(QWidget):
  layout = None
  
  def __init__(self, type='vertical'):
    super(Container, self).__init__()
  

  def _assign_layout(self, type):
    if type == 'vertical':
      self.layout = QVBoxLayout()
    elif type == 'horizontal':
      self.layout = QHBoxLayout()
    elif type == 'grid':
      self.layout = QGridLayout()