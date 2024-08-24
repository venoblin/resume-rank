from textblob import TextBlob 
from utils import read_text_file

def main():
  content = read_text_file('debug/test.txt')

  blob = TextBlob(content)
  keywords = blob.noun_phrases
  print(keywords)

if __name__ == '__main__':
  main()