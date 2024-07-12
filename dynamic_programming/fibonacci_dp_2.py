class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        value1 = 0
        value2 = 1

        for i in range(2, n + 1):
            current = value1 + value2
            value1 = value2
            value2 = current
        
        
        return value2