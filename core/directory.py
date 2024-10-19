import os
from core.file import File

class Directory(File):
  src: str
  
  def __init__(self, src: str):
    self.src = src

  def get_files(self):
    files = []

    for file_name in os.listdir(self.src):
      file_path = os.path.join(self.src, file_name)

      if os.path.isfile(file_path):
        files.append({
          'file_path': file_path,
          'file_name': file_name
        })

    return files