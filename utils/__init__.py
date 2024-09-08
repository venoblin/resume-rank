from textblob import TextBlob
import os

def run_command(command):
  return os.system(command)

def create_text_file(path, name, text):
  run_command(f'touch {path}/{name}.txt')
  run_command(f'echo {text} > {path}/{name}.txt')
    
def extract_keywords(text):
  blob = TextBlob(text)
  return blob.noun_phrases

def compare_keywords(job_keywords, resume_keywords):
  intersection = set(job_keywords).intersection(set(resume_keywords))
  union = set(job_keywords).union(set(resume_keywords))
  score = len(intersection) / len(union)
  return score
