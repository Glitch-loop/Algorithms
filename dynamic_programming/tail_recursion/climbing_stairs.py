"""
Climbing stairs

  A possible solution for this problem is the 
  recursive solution.

  Since there are two possible options to climb the stair
  (1 and 2 steps), the math expresion to know the number of possibilities to reach the top is:

  f(n - 2) + f(n - 1)

  The logic behind this solution is that all the cases 
  depends on "n" (n means the current step of the stair),
  in this way it is only needed to be subtracting until you 
  reach to "0" (top of the stair) to return 1 (that means 
  that there was found a solution).
   
"""
class Solution(object):
    def climbStairs(self, n):
      """
      :type n: int
      :rtype: int
      """
      if n==0:
          return 1
      else:
          if n - 2 >= 0:
              return self.climbStairs(n - 2) + self.climbStairs(n - 1)
          else: 
              return self.climbStairs(n - 1)
          
def main():
  s = Solution()
  print(s.climbStairs(2)) # 2
  print(s.climbStairs(3)) # 3
  print(s.climbStairs(4)) # 5
  print(s.climbStairs(38)) # 5


main()