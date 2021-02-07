class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid,r,c):
            grid[r][c] = "0"
            nx,ny = len(grid),len(grid[0])
            for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=x<nx and 0<=y<ny and grid[x][y]=="1":
                    dfs(grid,x,y)
        res = 0
        nr,nc = len(grid),len(grid[0])
        if nr == 0:
            return 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]=="1":
                    res+=1
                    dfs(grid,i,j)
        return res
