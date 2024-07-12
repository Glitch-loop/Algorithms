class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        thisDict = {}
        arr_sol = []

        # Convert nums array into a dictionary
        # [times of num in arr 1, and times in num in arr 2]
        for item in nums1:
            if item in thisDict:
                thisDict[item][0] += 1
            else:
                thisDict[item] = [1,0]

        # Finding intersections
        for item in nums2:
            if item in thisDict:
                thisDict[item][1] += 1

        # Converting the dictionary into an array
        for item in thisDict:
            if thisDict[item][0] > 0 and thisDict[item][1] > 0:
                times_in_arr_1 = thisDict[item][0]
                time_in_arr_2 = thisDict[item][1]
                arr_sol = arr_sol + ([item] * min(times_in_arr_1, time_in_arr_2))
                
        return arr_sol
