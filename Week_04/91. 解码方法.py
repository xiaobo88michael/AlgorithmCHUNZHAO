class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0]*n
        if s[0]=='0':
            dp[0]=0
        else:
            dp[0]=1
        
        for i in range(1,n):
            if s[i]!='0':
                t1 = dp[i-1]
            else:
                t1 = 0
            if i-2>=0:
                t2 = dp[i-2]
            else:
                t2 = 0
            if int(s[i-1:i+1])<=26 and s[i-1:i+1][0]!='0':
                
                dp[i]=t1 + t2
            else:
                dp[i]=t1
            if i-2<0 and int(s[i-1:i+1])<=26 and s[i-1:i+1][0]!='0':
                    dp[i]+=1
            
            
        return dp[-1]
