class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c,r = len(grid),len(grid[0])
        dp = [[0]*r for _ in range(c)]
        dp[0][0]=grid[0][0]

        for i in range(1,r):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        
        for j in range(1,c):
            dp[j][0]=dp[j-1][0]+grid[j][0]
        
        for i in range(1,c):
            for j in range(1,r):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        
        return dp[-1][-1]
