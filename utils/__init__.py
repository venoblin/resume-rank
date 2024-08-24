from textblob import TextBlob 

def read_text_file(path):
  try:
    with open(path, 'r') as file:
      content = file.read()
      return content
  except FileNotFoundError:
    return None
  
def extract_keywords(description):
  blob = TextBlob(description)
  return blob.noun_phrases