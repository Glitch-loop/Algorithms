class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        
        # Initialize dp array
        dp = [False] * (len(s2) + 1)
        dp[0] = True
        
        # Initialize the dp array for the base case when s1 is empty
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        
        # Fill the dp array
        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[-1]

# Example usage
sol = Solution()
print(sol.isInterleave("aab", "axy", "aaxaby"))  # Output: True
print(sol.isInterleave("aa", "ab", "aaba"))      # Output: True
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # Output: True
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # Output: False
