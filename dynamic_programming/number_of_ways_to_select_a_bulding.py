"""
This is the 2222nd problem of leetcode called Number of ways to select a building.

Key concept: prefix array.

"""

class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s) 
        arr_1s = [0] * s_len
        arr_0s = [0] * s_len
        count_1s = 0
        count_0s = 0
        combinations = 0

        # Calculate prefix array
        for i in range(s_len):
            char = s[i]
            if char == "1":
                count_1s += 1
            else:
                count_0s += 1
              
            arr_1s[i] = count_1s
            arr_0s[i] = count_0s

        # Calculate the possibilities for each position
        for i in range(s_len):
            char = s[i]
            if char == "1":
                before = arr_0s[i]
                after = arr_0s[s_len - 1] - before
                combinations = combinations + before * after
            else:
                before = arr_1s[i]
                after = arr_1s[s_len - 1] - before
                combinations = combinations + before * after


        return combinations