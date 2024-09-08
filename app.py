from utils import extract_keywords, compare_keywords, read_file

def main():
  job = read_file('debug/job.txt')
  resume = read_file('debug/resume1.pdf')

  print(job)

if __name__ == '__main__':
  main()