from gui.resume_manager import ResumeManager
from core.file import Files

def main():
  dir = Files('files/resumes')
  
  app = ResumeManager()
  app.run()

if __name__ == '__main__':
  main()