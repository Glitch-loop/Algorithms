from collections import deque

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        queue = deque()
        counter = k

        # Initialazing queue
        for i in range(1, n + 1):
            queue.append(i)


        while len(queue) > 1:
            counter -= 1
            item = queue.popleft()

            if counter > 0:
                queue.append(item)
            else:
                counter = k
        
        return queue[0]