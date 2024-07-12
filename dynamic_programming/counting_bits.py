"""
The problem consist in counting all the "1" in binary number resulted of convert the current number 
to its binary representation, the numbers are 0 to n.

Each "result" of the addition is going to be stored in an array and returned altogether

For example for the input 2.

n = 2
Output [0,1,1]

n = 5
Output: [0,1,1,2,1,2]

Solution:

For this problem there are two solutions, the first is througth bit manipulation, and the 
second one is using dynamic programming.

At least the solution that I could get its complexity is O(n).

But first it is worth to review the brute force solution:
  In this solution you have to iterate from 0 to n, then each number has to be converted in its
  binary representation and then you have to handle it as a string, counting all the number
  in the binary representation.
  This solution has a complexity of O(n^2) 

Dynamic programming approach:
1. Visualize the problem.
If you see the numbers in its decimal form they will give you few information, so it is convenint 
to convert them into a binary representation and format it like in a table.
The table is going to be extended to n=16

0  =      0
1  =      1
2  =     10
3  =     11
4  =    100
5  =    101
6  =    110
7  =    111
8  =   1000
9  =   1001
10 =   1010
11 =   1011
12 =   1100
13 =   1101
14 =   1110
15 =   1111
16 =  10000

2. Establish the sub-problems
First it is important to analyze the sequence, if you pay attention, the greatest numbers
has inside of them previous calculated numbers, for example:
2  =     10
6  =    110
or
3  =     11
11 =   1011

Here, as we want to know the number of "1" in each number, we can go back to those number
and retrieve the result of the previous calculation.

Written as a problem might be:
  How many "1" has the number that compouse the current nunmber.

So we can use this subproblem to solve the complex problem.

3. Generalization

Once we identified the subproblem, we need to generalize them... 
Analizing there are 2 options:
  - String manipulation (inefficient).
  - Mathematical sequence.

In the first one, if you remove the first 1 (after the number 2 in decimal), 
you always going to have the index that you need to consult to satisfy the problem, 
but it leads to O(n^2) solution

Now, the math approach is better, if you see the bytes representation of the problem
you are going to see that from certain numbers it is added a new bit, that means
that before of add that new bit there is a range to represent the number "lower"
than the number which the bit is added.

So that means that if you subtract the number (that can be senn like index), you will
get the correct index to consult.
Now if you look the sequence, you are going to realize that those number belongs to the  following 
sequence: 
  2^N

We can use to determine the range for each number, you have only to use this formula within a for,
if the current number belongs to the sequence update the number for the next digit N+1, it will
give you the new range of number.

Now with the current result of the formula, you only have to substract from i to get the number
to retrieve.
"""
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        
        dp = []
        dp.append(0)
        dp.append(1)

        sequence = 1
        pivot = 2**sequence

        for i in range(2,n + 1):
            dp.append(dp[i - pivot] + 1)

            if i == pivot:
                sequence += 1
                pivot = 2**sequence

        return dp
