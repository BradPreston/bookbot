import sys
from stats import get_num_words, get_characters, sorted_dict

def get_book_text(file_path):
  print(f"Analyzing book found at {file_path}")
  with open(file_path) as f:
    file_contents = f.read()
    get_num_words(file_contents)
    characters = get_characters(file_contents)
    char_count = sorted_dict(characters)
    
    for dict in char_count:
      print(f"{dict.get('char')}: {dict.get('num')}")
        

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  file_path = sys.argv[1]
  print("============ BOOKBOT ============")
  get_book_text(file_path)
  print("============= END ===============")

main()