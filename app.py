from core.file import File
from utils import compare_keywords

def main():
  job = File('debug/job.txt')
  resume = File('debug/resume.txt')

  job_keywords = job.extract_keywords()
  resume_keywords = resume.extract_keywords()

  print(compare_keywords(job_keywords, resume_keywords))

if __name__ == '__main__':
  main()