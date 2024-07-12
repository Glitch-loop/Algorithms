"""
This solution corresponds to the problem 22th called generate parenthesis.

In this we have to return all the possible "well-formed" parenthesis combinations, depending on 
a given integer input; The integer represent the "pairs" of parenthesis.

Here is an example:
  n = 3
  output = ["((()))","(()())","(())()","()(())","()()()"]

Solution:
This problem can be solved using backtraking.

Since we have only 2 possibilities to call in the recursive function one for "(" and other for ")",
we can keep tracing of the remainding parenthesis in the recursive function.

So, the recursive function will have 3 parameters:
  - op (open parenthesis): Used to count the number of remainind open parenthesis.
  - cp (closed parenthesis): Used to store the number of parenthesis to be closed.
  - string: To keep track of the combination achieved at the moment.

So since eventualy, both variables will converge to "0" (indicating that there is not more 
possibilities for open parenthesis, and all the parenthesis were closed), we can consider this as
our base case.

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arrSol = []

        def dfs(op, cp, s):
            
            if op == 0 and cp == 0:
                print(s)
                arrSol.append(s)
                return
            
            if op > 0:
                dfs(op - 1, cp + 1, s + "(")
            
            if cp > 0:
                dfs(op, cp - 1, s + ")")

        dfs(n, 0, "")
        return arrSol

        