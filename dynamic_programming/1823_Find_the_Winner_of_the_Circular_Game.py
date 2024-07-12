class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 0
        for player_num in range(2, n + 1):
            res = (res + k) % player_num
            print("player_num:",  player_num)
            print("res:",  res)
        return res + 1