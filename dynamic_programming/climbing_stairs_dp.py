
class Solution(object):
    def climbStairs(self, n):
      """
      :type n: int
      :rtype: int
      """
      if n == 0:
        return 0
      
      if n == 1:
         return 1

      # Creating the array to store the solutions of the 
      # suproblems
      # The size depends on "n": the number of step in the 
      # stair. 
      dp = [0] * (n + 1)

      # Initializing array.
      dp[0] = 1
      dp[1] = 1

      # Calculating the solution
      for i in range(2, n + 1):
        # Calculating solution for the subproblem.
        # Remember that the math function that describes the
        # solution of the problem is: f(n - 1) + f(n - 2)
        dp[i] = dp[i - 1] + dp [i - 2]
      

      return dp[n]

        
