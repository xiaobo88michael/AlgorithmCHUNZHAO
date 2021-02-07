class Solution(object):
    
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def dfs(board,x,y):
            count = 0
            nx,ny = len(board),len(board[0])

            for i in range(8):
                tx,ty = x+dirx[i],y+diry[i]
                if tx<0 or tx>=nx or ty<0 or ty>=ny:
                    continue
            
                if board[tx][ty]=="M":
                    count+=1
            
            if count>0:
                board[x][y]=str(count)
            else:
                board[x][y]='B'
        
                for i in range(8):
                    tx,ty = x+dirx[i],y+diry[i]
                    if tx<0 or tx>=nx or ty<0 or ty>=ny or board[tx][ty]!='E':
                        continue
                    dfs(board,tx,ty)
        dirx = [0,1,0,-1,1,1,-1,-1]
        diry = [1,0,-1,0,1,-1,1,-1]
       
        x,y = click[0],click[1]

        if board[x][y]=="M":
            board[x][y]="X"
        else:
            dfs(board,x,y)
        
        return board
