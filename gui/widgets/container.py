from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QWidget

class Container(QWidget):
  layout: QVBoxLayout | QHBoxLayout | QGridLayout
  type = ''
  
  def __init__(self, type='vertical'):
    super().__init__()
    self.type = type
    self._assign_layout(self.type)

    self.setLayout(self.layout)

  def _assign_layout(self, type):
    if type == 'vertical':
      self.layout = QVBoxLayout()
    elif type == 'horizontal':
      self.layout = QHBoxLayout()
    elif type == 'grid':
      self.layout = QGridLayout()

  def clear_layout(self):
    while self.layout.count():
        item = self.layout.takeAt(0)  
        widget = item.widget()
        
        if widget is not None:
            widget.deleteLater()