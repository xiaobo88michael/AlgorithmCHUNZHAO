class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            temp=0
            while i:
                i&=(i-1)
                temp+=1
            res.append(temp)
        
        return res
