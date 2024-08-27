from utils import read_text_file, extract_keywords, read_pdf_file

def main():
  desc = read_text_file('debug/desc.txt')
  desc_keywords = extract_keywords(desc)

  print(desc_keywords)

  
if __name__ == '__main__':
  main()