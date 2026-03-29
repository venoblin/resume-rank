from core.utils import run_command

def main():
  run_command('mkdir files')
  run_command('mkdir files/resumes')
  run_command('python -m spacy download en_core_web_trf')

if __name__ == '__main__':
  main()