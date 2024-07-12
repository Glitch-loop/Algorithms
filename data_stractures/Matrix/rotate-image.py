class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
          This solution is composed by two small solution; The first sub-problem is to find
          the new position of the current element (rotation) and the second sub-problem, derived
          from the first problem, it is to save that "destine position" where previous element 
          have taken after the rotation.

          In the case of the first sub-problem it is needed to use an "sequence" that is going to 
          be substracting along the traverse of the rows.
          This substraction depends mainly in the row that is currently the iteration.

          For the second sub-problem, that is when the position is taken to save the rotation of a 
          previous element, it is needed an auxiliar data structure to store those values that are
          overlapped.
          It works because the traversing of the matrix will eventually traverse for all the 
          positions, so if there is a position on which its original value was replaced by the 
          rotation of a previous value, we have to ask to the data structure to get the value
          that was missing in the matrix.
          
        """

        thisDict = {}
        n = len(matrix)

        # Start sequence
        i_sequence = 0
        j_sequence = n - 1

        for i in range(n):
            i_rate = i_sequence
            j_rate = j_sequence
            for j in range(n):
                # Getting the destine position to for the current value
                rotate_i = i + i_rate
                rotate_j = j + j_rate

                # Getting the keys for the current roatio.
                overlapped_value_key = str(rotate_i) + "," + str(rotate_j)
                value_to_rotate_key = str(i) + "," + str(j)


                if rotate_i >= i and rotate_j >= j or rotate_i >= i and rotate_j < j:
                    # Position that hasn't been traversed, therefore, overlapped 
                    # values.                    
                    thisDict[overlapped_value_key] = matrix[rotate_i][rotate_j]
                
                # Rotating the image
                if value_to_rotate_key in thisDict:
                    # Overlapped value case
                    value = thisDict[value_to_rotate_key]
                    matrix[rotate_i][rotate_j] = value
                    del thisDict[value_to_rotate_key]
                else:
                    # Normal rotation
                    matrix[rotate_i][rotate_j] = matrix[i][j]

                i_rate += 1
                j_rate -= 1

            i_sequence -= 1
            j_sequence -= 1
        


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):  #transpose
            for j in range(i+1):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(n):    #reverse of rows
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
        