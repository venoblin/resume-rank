from core.file import File

def main():
  job = File('debug/job.txt')
  resume = File('debug/resume1.pdf')

  print(job.extract_keywords())

if __name__ == '__main__':
  main()