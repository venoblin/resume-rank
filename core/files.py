import os
from PyPDF2 import PdfReader
from textblob import TextBlob

class Files:
  src = ''
  content = ''
  file_extension = ''
  
  def __init__(self, src: str = '') -> None:
    self.src = src

    if os.path.isdir(src):
      self.file_extension = 'dir'
    else:
      self.file_extension = os.path.splitext(self.src)[1].lower()

    try:
      if self.file_extension == 'dir':
        print('dir')
      elif self.file_extension == '.txt':
        with open(self.src, 'r') as file:
          output = file.read()
          self.content = output
      elif self.file_extension == '.pdf':
        reader = PdfReader(self.src)
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
    if self.file_extension == 'dir':
      return 'Error: Source is not a file!'
    
    return self.content
  
  def extract_keywords(self):
    if self.file_extension == 'dir':
      return 'Error: Source is not a file!'
    
    blob = TextBlob(self.content)
    return blob.noun_phrases
  
  def get_files(self):
    if self.file_extension != 'dir':
      return 'Error: Source is not a directory!'
    
    files = []

    for file_name in os.listdir(self.src):
        file_path = os.path.join(self.src, file_name)

        if os.path.isfile(file_path):
            files.append({
              'file_path': file_path,
              'file_name': file_name
            })

    return files