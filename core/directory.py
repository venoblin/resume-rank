import os

class Directory:
  src: str
  files = []
  
  def __init__(self, src: str):
    self.src = src

    for file_name in os.listdir(self.src):
      file_path = os.path.join(self.src, file_name)

      if os.path.isfile(file_path):
        self.files.append({
          'file_path': file_path,
          'file_name': file_name
        })
    print('hi')

  def get_files(self):
    return self.files
