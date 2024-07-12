class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        # def is_nice(sub):
        #     return all(c.lower() in sub and c.upper() in sub for c in sub)
        
        def divide_and_conquer(sub):
            if len(sub) < 2:
                return ""
            for i, c in enumerate(sub):
                print(sub)
                print(c)
                if c.lower() not in sub or c.upper() not in sub:
                    left = divide_and_conquer(sub[:i])
                    right = divide_and_conquer(sub[i + 1:])
                    return left if len(left) >= len(right) else right
            return sub
        
        return divide_and_conquer(s)