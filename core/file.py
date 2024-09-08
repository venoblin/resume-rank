import os
from PyPDF2 import PdfReader

class File:
  file_source: str
  content: str
  
  def __init__(self, file_source: str = '') -> None:
    self.file_source = file_source
    file_extension = os.path.splitext(self.file_source)[1].lower()

    try:
      if file_extension == '.txt':
        with open(self.file_source, 'r') as file:
          output = file.read()
          self.content = output
      elif file_extension == '.pdf':
        reader = PdfReader(self.file_source)
        output = ''

        for i in range(len(reader.pages)):
          page = reader.pages[i]

          if i == 0:
            output += page.extract_text()
          else:
            output += f' {page.extract_text()}'

        self.content = output
    except FileNotFoundError:
      print('Error: File not found!')
      return None

  def read_file(self):
    return self.content
