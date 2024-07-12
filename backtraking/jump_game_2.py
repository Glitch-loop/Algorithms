"""
Problem of Leetcode: Jump Game II

This is a possible solution for the 45th problem of leetcode called Jump Game II.
It was followed a backtraking approach, first it is necessary to understand the problem.

The problem is:
  Given a 0-indexed array of length nm use the value of each cell to get to the final position of the array.

Constraints:
  - 0 <= j <= nums[i]
    The value of the jumps will range between 0 and the value of the current cell in the array. 

  - i + j < n
    It is not possible be get a value grater than the length of the array.

    
Example: 
  Input: [2,3,1,1,4]
  Ouput: 2

  Explanation:
    It is a matter of fact that we always going to start in the position "0", following this, we have 2
    options:
      1. Jump to the cell 1; 0 + 1 = current index + jump
      2. Jump to the cell 2; 0 + 2 = current index + jump
    
    With this in mind, we can determine that the shortest path to reach the last element is:
    0 + 1 = 1
    1 + 3 = 4

      Operations 2 (in other words number of jumps).

    Remember that the result of the additions are the index on which we fell. 

Backtracking Solution:
  Saying that, we can recursively solve this problem just trying all the paths (discarding those that don't follow: i + j < n),
  and when we get to the final of the array, the results can be stored in an array of results.

  After the recursive function, it is just needed to search in the array of solutions and take the one with the fewest jumps.
"""

import sys
class Solution(object):
    """
      Time complexity: O(2^N)
      Space complexity: O(N)
    """
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_len = len(nums)

        # If there is not nodes or just 1, it doesn't make sense to find a path.
        if arr_len == 0 or arr_len == 1:
            return 0
        
        jump = sys.maxsize
        solution = []
        
        def dfs(current_node, path):
            # Remember that the value of the current possition is the possible paths that we can take.
            possible_paths = nums[current_node]
            # Explore the possible paths.
            for i in range(1, possible_paths + 1):
                # Remember, to define a jump is the additon of the current position plus the possible jump.
                next_node = current_node + i
                if next_node < arr_len:
                    # If is true, it is a valid jump.
                    if next_node == arr_len - 1:
                        # If we get to the last element of the array, store the solution in the array of solution.
                        solution.append(path + 1)
                        return
                    else:  
                        # Explore recursively the paths of the next node.
                        dfs(next_node, path + 1)
        
        dfs(0,0)

        for item in solution:
            if item < jump:
                jump = item

        return jump
