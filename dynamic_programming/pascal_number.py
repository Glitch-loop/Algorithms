"""
Pascal's triangule is a "problem" that utilizes dynamic programming. This is true because we need 
the previous calculations to compute the current ones which encourage  the use of
dynamic programming).

It may be tempting try to find where we can apply "dynamic programming", but the algorithm itself
to calculate the Pascal's triangle inherently implements this technique.

Another approach to solving this problem is using recursion. However, remember that
dynamic programming is an optimization of recursion. Additionally, since this problem can be solved
using the buttom-up approach, the solution is iterative, which is more "efficient" terms of resources conspumtion during execution.
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        solution = []
        for i in range(numRows): # This for means the current row
            # Creating the new row
            # The length is determined by adding "1" to the current index, here the index means
            # the current row... It is a pascal propierty.
            solution.append([1] * (i + 1))
            
            for j in range(1,i):
            # We always starts in 1, because the first element always going to be "1".
            # And we finish one element before the final by the same reason.

                solution[i][j] = solution[i-1][j-1] + solution[i-1][j]

        return solution