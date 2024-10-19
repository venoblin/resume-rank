import os
from PyPDF2 import PdfReader
from textblob import TextBlob

class File:
  src: str
  content: str
  file_extension: str
  
  def __init__(self, src: str = '') -> None:
    self.src = src
    self.file_extension = os.path.splitext(self.src)[1].lower()

    try:
      if self.file_extension == '.txt':
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
    return self.content
  
  def extract_keywords(self):    
    blob = TextBlob(self.content)
    return blob.noun_phrases