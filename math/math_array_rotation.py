class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        num_rotation = k % len_nums

        if num_rotation == 0:
            return

        partition = len_nums - num_rotation

        nums[:] = (nums[partition:] + nums[:partition])[:]
