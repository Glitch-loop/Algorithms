"""
  1509. Minimum Difference Between Largest and Smallest Value in Three Moves
"""
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 4:
            return 0

        nums.sort()
        minVal = sys.maxsize

        minVal = min(minVal, nums[n-4] - nums[0])
        minVal = min(minVal, nums[n-1] - nums[3])
        minVal = min(minVal, nums[n-2] - nums[2])
        minVal = min(minVal, nums[n-3] - nums[1])

        return minVal
