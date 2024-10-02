from gui.widgets.label import Label

class HeaderLabel(Label):
  def __init__(self, text=''):
    super(HeaderLabel, self).__init__(text)

    font = self.font()
    font.setPointSize(30)
    font.setBold(True)

    self.setFont(font)