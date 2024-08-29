from textblob import TextBlob
from PyPDF2 import PdfReader
import os

def run_command(command):
  return os.system(command)

def read_file(path):
  file_extension = os.path.splitext(path)[1].lower()

  try:
    if file_extension == '.txt':
      with open(path, 'r') as file:
        content = file.read()
        return content
    elif file_extension == '.pdf':
      reader = PdfReader(path)
      output = ''

      for i in range(len(reader.pages)):
        page = reader.pages[i]

        if i == 0:
          output += page.extract_text()
        else:
          output += f' {page.extract_text()}'

      return output
  except FileNotFoundError:
    print('Error: File not found!')
    return None

def read_text_file(path):
  try:
    with open(path, 'r') as file:
      content = file.read()
      return content
  except FileNotFoundError:
    print('Error: File not found!')
    return None
  
def create_text_file(path, name, text):
  run_command(f'touch {path}/{name}.txt')
  run_command(f'echo {text} > {path}/{name}.txt')
  
def read_pdf_file(path):
  try:
    reader = PdfReader(path)
    output = ''

    for i in range(len(reader.pages)):
      page = reader.pages[i]

      if i == 0:
        output += page.extract_text()
      else:
        output += f' {page.extract_text()}'

    return output
  except FileNotFoundError:
    print('Error: File not found!')
    return None
    
def extract_keywords(text):
  blob = TextBlob(text)
  return blob.noun_phrases

def compare_keywords(job_keywords, resume_keywords):
  intersection = set(job_keywords).intersection(set(resume_keywords))
  union = set(job_keywords).union(set(resume_keywords))
  score = len(intersection) / len(union)
  return score
