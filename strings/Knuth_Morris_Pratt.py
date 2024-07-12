"""
Date: 06-15-24

Knuth Morris Pratt


This algorithm is used to find occurrences of a pattern in a text.

Complexity: O(n+m)
  n: Length of text
  m: Length of pattern

Used propierty:
  - Degenerating property: Pattern having the same sub-patterns appearing more than
    onde in the pattern.

How does it works?
The basic idea behaind this algorithm is to skip characters in text using the sub-patterns
found in the pattern.

This algorithm is divided in 2 main steps:
1. Compute the lps array (Find the sub-pattern and therefore knowing how many characters be can skip)
2. Use lps array in the search to skip those characters that are not necessary to evaluate.

https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
"""


"""
  This function pre-processes the pattern before of comparing with the string.
  Thanks to the lps[] array, which contains the number of letter to be skipped, is that 
  the match pattern can be optimized, avoiding revalidation multiple cases.
"""
def prefix_function(pattern):
  # Creating lps[] array
  # Note: lps comes from longest prefix suffix

  # Creating variables needed for the algorithm
  lps = [0] * len(pattern) # Array to store the calculations
  lenPrefix = 0 # Array to store the length of the patterns found
  # Iterator. It starts is initialized with 1, because "0", which is the first letter, has 
  # already covered
  i = 1 

  # Initializing lps. Since we haven't begun to analyze the pattern, it is always going to start in 
  # 0. 
  lps[lenPrefix] = 0

  while(i < len(pattern)):
    if pattern[lenPrefix] == pattern[i]:
      # That means that there is a match in the prefix (lenPrefix) and the suffix (i)
      lenPrefix += 1
      lps[i] = lenPrefix
      i += 1
    else:
      if lenPrefix > 0:
        # That means that there was not a match between the prefix and the suffix.
        # So, lenPrefix is not 0 (there are other letter in the prefix), there is the
        # Possibility
        lenPrefix = lps[lenPrefix - 1]
      else:
        lenPrefix = 0
        lps[i] = lenPrefix
        i += 1

  return lps


"""
Once you have the lps arrays, you only have to make an linear search comparing the current letter
of the text with the current letter of the pattern.

The difference is when you detect that there is no match between both iterator, you have just to use
lps to know how many characters you can skip.

Remember for each character in the pattern, there is an value in lps indicating the number of 
characters to skip.
"""
def find_match(text, lps, pattern):
  i = 0
  j = 0

  while(i < len(text)):
    if text[i] == pattern[j]:
      i += 1
      j += 1
    else:
      i += lps[j]
      j = 0

    if j == len(pattern):
      print(text[i - len(pattern):i])
      print("Pattern found")
      j = 0


def main():
  lps = prefix_function("ABABC")
  find_match("ABABABABCAAA", lps, "ABABC")

main()
