"""
  Z algorithm
  Date: 06-15-24
  
  Z algorithm is used to find pattern inside a text.

  It is similar to KMP regarding to "avoid" unnecesary comparisions. 
  While KMP "skips" characters using a pre-proccesed array (which has the number of skips to make 
  according to the degradation propierty), Z algorithm uses previous computed results to calculate
  the number of matches that is going to have the character of the current position.

  This algorithm is a combination between sliding window and dynamic programing because it uses 
  previous computations to calculate new ones, while it uses a "box" to determine if there is 
  possible to calculate the match instead of determine it explicily.

  
  Complexity: O(n+m)
  n: Text
  m: Pattern

  https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/

  https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm
"""

def z_algorithm(pattern, text):
  fullString = pattern + "$" + text
  z_arr = [0] * len(fullString)
  l = 0
  r = 0
  k = 1
  
  while(k < len(fullString)):
    if k < r:
      # The current character is inside of a match
      z_arr[k] = z_arr[k-l]
    else:
      # There is not a match
      # It is needed to compute explicitly
      i = 0
      j = k
      while(fullString[i] == fullString[j]):
        i += 1
        j += 1

      if i > 0 and j > k:
        # There was match therefore update the Z-box
        l = k
        r = j - 1 
      
      z_arr[k] = j - k

    k += 1 # Next character

  return z_arr


print(z_algorithm("aab", "aabxaaaz"))