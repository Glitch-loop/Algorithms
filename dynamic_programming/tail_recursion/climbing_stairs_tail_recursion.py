"""
  Climbing stairs.

  In this approach, the problem was solved using tail 
  recursion.

  This methodology consists in use previous results from past
  calls to be used in next calls.

  This type of recursion has the peculiarity that the last 
  "action" is the recursive "call".
  
  So, it is made different operations before calling a 
  recurise call.

"""
class Solution(object):
    def climbStairs(self, n):
      """
      :type n: int
      :rtype: int
      """
      return self.climbStairsTail(n,1,1)


    """
      steps_remaining: Number of steps for reach to 0
      a: Number of ways to reach the current step.
      b: Number of ways to reach the next setp

      a + b: Number of ways to reach the step after the next 
      step.
    """
    def climbStairsTail(self, steps_remaining, a, b):
        if steps_remaining==0:
          return a
        else:
          return self.climbStairsTail(steps_remaining - 1, b, a + b)
          
def main():
  s = Solution()

  print(s.climbStairs(2)) # 2
  print(s.climbStairs(3)) # 3
  print(s.climbStairs(4)) # 5
  print(s.climbStairs(38)) # 63245986


main()
