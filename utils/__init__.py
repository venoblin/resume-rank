from textblob import TextBlob
from PyPDF2 import PdfReader

def read_text_file(path):
  try:
    with open(path, 'r') as file:
      content = file.read()
      return content
  except FileNotFoundError:
    return None
  
def read_pdf_file(path, page):
  reader = PdfReader(path)
  page = reader.pages[page]
  return page.extract_text()
  
def extract_keywords(description):
  blob = TextBlob(description)
  return blob.noun_phrases