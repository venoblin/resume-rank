import os
from PyPDF2 import PdfReader
from textblob import TextBlob

class Files:
  src = ''
  content = ''
  
  def __init__(self, src: str = '') -> None:
    self.src = src
    file_extension = os.path.splitext(self.src)[1].lower()
    print(file_extension)

    try:
      if file_extension == '.txt':
        with open(self.src, 'r') as file:
          output = file.read()
          self.content = output
      elif file_extension == '.pdf':
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
  
  # @classmethod
  # def get
