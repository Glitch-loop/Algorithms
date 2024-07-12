class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        thisSet = set() 
        left = 0
        right = len(nums) - 1
        
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                # Different indexes
                if i != left and i != right and left != right:
                    result = nums[i] + nums[left] + nums[right] 
                    if(result == 0):
                        thisSet.add((nums[i], nums[left], nums[right]))
                        left += 1
                    elif(result < 0):
                        left += 1
                    else:
                        right -= 1
                else:
                    if i == left:
                        left += 1
                    
                    if i == right:
                        right -= 1
                    


        # Formating sets
        for item in thisSet:
            permutations.append([item[0], item[1], item[2]])

        return permutations