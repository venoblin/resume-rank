from utils import read_text_file, extract_keywords, read_pdf_file, compare_keywords

def main():
  desc = read_text_file('debug/desc.txt')
  desc_keywords = extract_keywords(desc)

  resume = read_pdf_file('debug/resume1.pdf')
  resume_keywords = extract_keywords(resume)

  score = compare_keywords(desc_keywords, resume_keywords)
  print(score * 100)


if __name__ == '__main__':
  main()