
def read_text_file(path):
  try:
    with open(path, 'r') as file:
      content = file.read()
      return content
  except FileNotFoundError:
    return None