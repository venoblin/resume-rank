import nltk
from core.utils import run_command

def main():
  run_command('mkdir files')
  run_command('mkdir files/resumes')
  run_command('python -m textblob.download_corpora')
  nltk.download('punkt_tab')

if __name__ == '__main__':
  main()