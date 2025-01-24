from collections import Counter

def anagrams_alternate_solution(s1, s2):
  return Counter(s1) == Counter(s2)
