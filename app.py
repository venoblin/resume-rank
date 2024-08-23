from utils import read_text_file

def main():
  content = read_text_file('debug/test.txt')
  print(content)

if __name__ == '__main__':
  main()