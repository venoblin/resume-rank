from core.file import File

def main():
  job = File('debug/job.txt')
  resume = File('debug/resume1.pdf')

  print(job.read_file())

if __name__ == '__main__':
  main()