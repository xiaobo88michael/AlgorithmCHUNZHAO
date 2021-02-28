class unionfind:
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0
    
    def find(self,x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets-=1

    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets +=1

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        uf = unionfind()
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i,j)
        
        return uf.num_of_sets
