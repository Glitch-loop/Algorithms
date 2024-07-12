"""
Explanation:
From a given number, get all the possible codifications using the following table:
A -> 1
B -> 2
C -> 3
...
Z -> 26

Example:
121
Possible codifications:
  1. 1-2-1
  2. 1-21
  3. 12-1

Output 3

Analyzing the problem, there are two constraints:
  1. It is not possible leading zeros: 06
  2. The combination of the number cannot be grater than 26 (that is the las element it the table 
  "z")

Brute force solution:
As it is a combinatorial problem, this problem can be solved using recursion.

It is a matter of fact that we always are going to start with the first "element", here
is where we have two cases:
  1. The number consit on one character.
  2. The element consist on two characters.

Since  previous elements are going to be used in subsequents results, we can resolve this 
using recursion.

The brute force solution is going to have two calls:
  - The first one taking the possibility of just one character.
  - The second one taking the possibilit of two characters.

The stop for this recursive calls will be 3:
  - Leading zero
  - Number grater than 26
  - Empty string (there are not characters to combinate)

For the first two cases will return 0, becuase are invalid ones.
For the last one, it will return 1, indicating that a path was found.


The recursion call is going to be like this:
121

            .
        1         12
     2    >21<       >1<
  >1<

It is a simple case, but it provides the idea of how it works, there are only 3 "satisfactory"
base case (on where doesn't remain characters to validate), so in this cases it will be returned 1
that as result with all the subproblems will be 3.

Problem with this solution:
Since there are two recursive calls (one for 1 character and one for 2 characters), the solution 
will have a complexity of O(N^2) because each recursive call calls two recursive calls.

This solution is prone to overflow the stack, and the time that would take for solving large inputs 
is too much (it is an inefficient algorithm).

Fortunately there is a better solution using dynamic programming that its time complexity is O(N)

Dynamic programming approach:
1. Visualiza the problem.
As was explained before, this problem can be represented using a "tree recursion"

In a first glimpse, there is not an overlapped sub-problems, but if see you will realize that 
there is a subproblem.

2. Identifying the sub-problem
The sub-problem here is for knowing the amount of correct combinations, we need to ask to the 
recursive call how many correct paths it was able to found.

If this is the input 
  112161

To know all the possible paths are in the first position, it is neede to ask to the next position
how many paths it was able to found:
  [112161]
    1[12161]
      12[161]

So that means that we can store previous solutions and use them to calculate more general ones.

3. Generalization
Since we indentified the subproblem and we were able to use their parcial solution to solve the 
principal solution.

It can be either recursive or iterative implementation, the issue here is that instead of waiting 
to get empty the string we are going to add to the current possition 1 if there is a one character 
case, and other 1 in case of two character case.

In this approach the calculation of both cases are calculated in the same iteration.

In the case of the recursive approach, the base case will be "n" that is the length of the input.
"""

class Recursive_Solution(object):
    def numDecodings(seld, s: str) -> int:
      dp = { len(s) : 1 }
      def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0

        res = dfs(i + 1)
        if (i + 1 < len(s) 
            and (s[i] == "1" or s[i] == "1" and s[i + 1] in "0123456")):
            res += dfs(i + 2)
        dp[i] = res
        return res
      return dfs(0)



class Iteravive_Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {len(s) : 1}

        # Starting from the last element.
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                # "Base case", it is not possible to have a leading zero
                dp[i] = 0 
            else:
                # Case on which the current number is only one.
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456")):
                # Case on which the current number is made up of two numbers.
                # Restriction: The number has to be lower than 26.
                dp[i] += dp[i + 2]
        
        return dp[0]