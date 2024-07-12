class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)

        if len_nums == 0:
            return 0
        elif len_nums == 1:
            return nums[0]
        elif len_nums == 2:
            return max(nums[0], nums[1])

        arr_sol = [0] * len_nums

        arr_sol[len_nums - 1] = nums[len_nums - 1]
        arr_sol[len_nums - 2] = nums[len_nums - 2]

        for i in range(len_nums - 3, -1, -1):
            first_option = i + 2
            second_option = i + 3

            first_sub_problem = 0
            second_sub_problem = 0

            if first_option < len_nums:
                first_sub_problem = arr_sol[first_option]

            if second_option < len_nums:
                second_sub_problem = arr_sol[second_option]
            
            arr_sol[i] = nums[i] + max(first_sub_problem, second_sub_problem)

        return max(arr_sol[0], arr_sol[1])
            

