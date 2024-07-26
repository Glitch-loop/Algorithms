"""
  Date: 07-26-24

  Problem:
    In a m x n grid, you have to find the total possible paths to arrive from the beginning to
    the last cell; top-left and bottom-right corner repectively.
    You can only move one step by iteration and that movement is constrained to go either
    down or right.

  Solution:
    It is a problem that can be solved using dfs, since you have to find the possible
    paths you can traverse the possibilities and then return the paths that you find.

    And well, where it is a backtraking solution, it is a DP solution. If you pay attention
    you can solve the main problem subdiving in small sub-problmes, in this case reducing the 
    space to search.

    So suppose that we have the following 3 * 7 grid

     0 1 2 3 4 5 6 
    0s
    1
    2            f

    If we start in the (2,5) position, the unique path to arrive to the final will be one and will
    be go down, the same thing will happen for (1,6) that will be go right.
    Here the out of bound can be interpreted as "0", since there is not an allowed area.
    
    Having this, we can conclude two things:
    1. The last row and column will be always 1 (since there is one possible way to get the final).
    2. We can know the amount the possible paths to get to the final asking to the previous 
    calculated positions, in this case adding the down and right possibility of the current 
    possition.


    The below declarations will be:

      0 1 2 3 4 5 6 
    0 s           1 0
    1      <- 3 2 1 0
    2 1 1 1 1 1 1 f 0
      0 0 0 0 0 0 0 <- not allowed


    In this way we can solve the problem calculating the rows from bottom to top, finishing 
    in the start position.
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        
        return row[0]