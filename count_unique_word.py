import re
from collections import Counter

def count_unique_word(file_name):
 text_string = open(file_name, 'r', encoding='utf-8').read().lower()
 match_pattern = Counter(sorted(re.findall(r'([\w\']+\w+)', text_string)))
 for words in match_pattern:
    print(f'{words}  {match_pattern[words]} times')

if __name__ == "__main__":
  count_unique_word('Book.txt')

