from utils import read_text_file, extract_keywords, read_pdf_file

def main():
  # content = read_text_file('debug/description.txt')
  # keywords = extract_keywords(content)
  # print(keywords)
  resume = read_pdf_file('debug/resume.pdf', 0)
  print(resume)

if __name__ == '__main__':
  main()