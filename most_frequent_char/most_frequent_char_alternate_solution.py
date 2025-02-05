from collections import Counter

def most_frequent_char_alternate_solution(s):
  count = Counter(s)
  most = None
  
  for char in s:    
    if most is None or count[char] > count[most]:
      most = char
  return most
