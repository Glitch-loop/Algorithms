def printMatrix(matrix):
  for row in matrix:
    print(row)

def longest_palindromic_substring(text):
  # Obtainig the lenght of the string
  n = len(text)
  
  start = 0 # Variable for storing the initial of the longest palindrome
  maxLenght = 1 # Variable for storing the mex size of the palindrome

  # Creating matrix
  rows, cols = n, n

  matrix = [[0 for _ in range(cols)] for _ in range(rows)] 

  # Checking subtrings of length 1
  for i in range(n):
    # Due to the start and end of the palindrome are the same letter, 
    # it is always going to be true.
    matrix[i][i] = 1
  

  # Checking substrings of length 2
  for i in range(n - 1):
    if text[i] == text[i + 1]: # Cheking the text
      matrix[i][i + 1] = 1
      # Store the current palindrome 
      # Since all the palindrome are of length 2, it doesn't matter what you are taking.
      start = i
      maxLenght = 2
  
  # Cheking subtring larger than 2
  for k in range(3, n + 1):
    print(k)
    # In the matrix, when it is finished a diagonal, the next diagonal is going to decrease 1 in 
    # lenght
    for i in range(n - k + 1):
      j = i + k - 1
      if (text[i] == text[j]) and matrix[i + 1][j - 1]:
        matrix[i][j] = 1
        print(k)
        if k > maxLenght:
          start = i
          maxLenght = k
      
  printMatrix(matrix)
  print(text[start:start + maxLenght])


longest_palindromic_substring("ccc")