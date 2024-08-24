from textblob import TextBlob 
from utils import read_text_file, extract_keywords

def main():
  content = read_text_file('debug/description.txt')
  keywords = extract_keywords(content)
  print(keywords)

if __name__ == '__main__':
  main()