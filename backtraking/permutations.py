class Solution(object):
    # O(n * n!)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums_len = len(nums)
        thisArr = []

        def recursive_permutation(permutation_level, chain):
            if permutation_level == nums_len - 1:
                # We found a permutation
                thisArr.append(chain[:])
                return

            for item in nums:
                if not(item in chain):
                    chain.append(item)
                    recursive_permutation(permutation_level + 1, chain)
                    chain.pop()


        for item in nums:
            recursive_permutation(0, [item])
        
        return thisArr