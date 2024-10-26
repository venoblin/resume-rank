from PySide6.QtWidgets import QPlainTextEdit, QStackedLayout
from gui.widgets.container import Container
from gui.widgets.header_label import HeaderLabel
from gui.widgets.button import Button
from core.directory import Directory
from core.file import File

class JobDescription(Container):
  textarea: QPlainTextEdit
  stack: QStackedLayout
  
  def __init__(self, stack):
    super().__init__()
    header = HeaderLabel(text='Job Description')
    self.stack = stack
    self.textarea = QPlainTextEdit()
    self.textarea.setPlaceholderText('Paste job description here...')
    find_btn = Button(text='Find Best Resume')
    find_btn.clicked.connect(self._find_resume_handler)

    self.layout.addWidget(header)
    self.layout.addWidget(self.textarea)
    self.layout.addWidget(find_btn)

  def _find_resume_handler(self): 
    content = self.textarea.toPlainText()
    all_resumes = Directory('files/resumes').get_files()

    resumes = []
    for idx, r in enumerate(all_resumes):
      score = File(r['file_path']).compare_keywords(content)
      new_resume = {**r, 'score': score}

      if len(resumes) > 0 and score >= resumes[idx-1]['score']:
        resumes.insert(0, new_resume)
      else:
        resumes.append(new_resume)
    
    self.stack.setCurrentIndex(1)
    resumes_checker = self.stack.currentWidget()
    resumes_checker.update_resumes(resumes)

