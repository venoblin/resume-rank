from utils import read_text_file, extract_keywords, read_pdf_file

def main():
  # desc = read_text_file('debug/description.txt')
  # desc_keywords = extract_keywords(desc)
  # print(desc_keywords)
  resume = read_pdf_file('debug/resume.pdf', 0)
  resume_keywords = extract_keywords(resume)
  print(resume_keywords)

if __name__ == '__main__':
  main()