class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        nx,ny = len(matrix[0]),len(matrix)

        if nx==0 or ny==0:
            return 0
        
        dp = [[0]*nx for _ in range(ny)]

        maxside = 0

        for i in range(ny):
            for j in range(nx):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                maxside = max(dp[i][j],maxside)
        
        return maxside*maxside
