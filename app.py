from utils import read_text_file, extract_keywords, read_pdf_file

def main():
  desc = read_text_file('debug/description.txt')
  desc_keywords = extract_keywords(desc)

  resume = read_pdf_file('debug/resume2.pdf')
  resume_keywords = extract_keywords(resume)

  print(desc_keywords)
  print(resume_keywords)
  
if __name__ == '__main__':
  main()