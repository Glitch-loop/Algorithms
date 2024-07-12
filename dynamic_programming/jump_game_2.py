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

  
Optimization (dynamic programming):
    Since it is possible to solve the problem recursively, it means that it will compute the same solution several times.
    So we can optimize the algorithm to same computation power storing the previous results using DP.

    Visualization:
        Since the problem can be represented as a graph, we can take advantege of this and ask us: I only need
        the best solution not all the possible solutions:
        array = [2,3,0,1,4]
        0: 1 -> 2
        1: 2 -> 3 -> 4 ->
        2: 
        3: 4
        4:

        *The value of the last element doesn't matter since any operation will be grater than "n", in addition, this element
        is the target element so it has nosense to make any operation.

    Sub-problem:
        From the previous visualization, we can formulate the next sub-problem:
            
            What is the path with the fewest jump to get to the last node from the current node?

    Establishing this problem we can create a solution from parcial solution, this is possible because the complete solution is going to 
    pass for the subpath with the fewest steps.

    Solution:
        We can make an array to store the parcial solutions and we are going to start from the end and go backwards to the first possition.
        This solution will be of the type of tabultation, and through we go backwards, we can retrieve the solution for the subproblem 
        that we previously calculated.
        


"""

import sys
class Solution(object):
    def jump(self, nums):
        # Time complexity: O(N^2)
        # Space complexity:O(N)

        """
        :type nums: List[int]
        :rtype: int
        """
        arr_len = len(nums)

        if arr_len == 0 or arr_len == 1:
            return 0
        
        dp = [0] * arr_len # Array to store the steps

        # Array to traverse all the nodes (sub problem), starting in the end and going to the frist element
        for current_node in range(arr_len - 2, -1, -1):
            # Possible paths for the current node.
            possible_paths = nums[current_node]

            # Local paths
            if possible_paths == 0:
                # Node doesn't have edges.
                local_path = 0
            else:
                # There are possible paths
                local_path = sys.maxsize

            for i in range(1, possible_paths + 1):
                next_node = i + current_node
                if next_node <= arr_len - 1:
                    # Valid jump
                    if next_node == arr_len - 1:
                        # That means that the jump get to the target node, the last one.
                        # If a jump from the current node get to the last one, it always going to be considered as 1 = 1 jump.
                        local_path = dp[next_node] + 1
                        break # It has nosense to explore other solutions, since we arrive to the last one.
                    else:  
                        if dp[next_node] > 0:
                            # Node with a possible solution.
                            # From all the nodes that we will explore, we are going to store the path with the fewest jumps.
                            local_path = min(local_path, dp[next_node] + 1)
            dp[current_node] = local_path


        return dp[0]
