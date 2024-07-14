"""
  What is the problem about?

  This problem states that given an array of length n, you have to split
  nums[i] into a 2 positive new integers, you can make the division at least "maxOperation".

  Your objetive is to minimize as most as possible the numbers of the array.


  Example:
  maxOperations = 2
  nums = [9]

  [9]
  [6,3]
  [3,3,3]

  Output: [3,3,3]
  
  Notice that you could divide 9 in such way that the output gave 4 and 5, but 
  you get the minimum possible number dividing firstly in such way that you get 
  3 and 6.


  Solution:

  The solution of this problem is using a binary search, this because the problem 
  accomplish this propierty:
  
  - The greater the number, less operations are needed to minimiza that number

  - (and vice versa) the lower the number, more operations will be needed to minimize the 
  number

  This problems follows an increasing or decreasing monotonic behavior.
  
  https://www.youtube.com/watch?v=znZ4wT1L8Y0&ab_channel=HappyCoding
"""


class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def helper(mid):
            cnt = 0
            print("mid: ", mid)
            for num in nums:
                print((num-1) // mid)
                cnt += (num-1) // mid
            
            return cnt <= maxOperations

        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            print(mid)
            if helper(mid): 
                l = mid + 1
            else:
                r = mid
        return l        
    


def main():
  s = Solution()
  s.minimumSize([9], 2)

main()