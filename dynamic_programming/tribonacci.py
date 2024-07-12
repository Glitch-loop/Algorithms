class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        # Create array of solutions (tabulation)
        dp = [0,1,1]

        p1 = 0
        p2 = 1
        p3 = 2


        for i in range(3, n + 1):
            solution = dp[p1] + dp[p2] + dp[p3]
            dp.append(solution)
            p1 += 1
            p2 += 1
            p3 += 1

        return dp[len(dp) - 1]