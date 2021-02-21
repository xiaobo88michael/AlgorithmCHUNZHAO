class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0]*n

        if n==0:
            return 0
        
        for i in range(n):
            if s[i]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                dp[i] = 2+dp[i-1]+dp[i-dp[i-1]-2]
        
        return max(dp)
