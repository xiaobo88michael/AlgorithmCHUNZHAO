class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dic = dict()
        for i in range(len(stones)):
            dic[stones[i]]=set()
        dic[stones[0]].add(0)

        for i in range(len(stones)):
            for k in dic[stones[i]]:
                for j in range(k-1,k+2):
                    if j>0 and stones[i]+j in dic:
                        dic[stones[i]+j].add(j)
        
        return len(dic[stones[-1]])>0
