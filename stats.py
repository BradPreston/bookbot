def get_num_words(string):
  print("----------- Word Count ----------")
  num_words = len(string.split())
  print(f"Found {num_words} total words")

def get_characters(string):
  print("--------- Character Count -------")
  characters = {}

  for char in list(string):
    if char.lower() in characters:
      characters[char.lower()] += 1
    else:
      characters[char.lower()] = 1
  
  return characters

def sort_on(items):
  return items["num"]

def sorted_dict(dict):
  dict_list = []
  for char, count in dict.items():
    if (char.isalpha()):
      dict_list.append({ "char": char, "num": count })
  
  dict_list.sort(reverse=True, key=sort_on)

  return dict_list