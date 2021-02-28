import numpy as np
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def matPow(p,n):
            ret = np.mat([[1,0],[0,1]])

            while n:
                if n&1==1:
                    ret = np.dot(ret,p)
                n>>=1
                p = np.dot(p,p)
            
            return ret
        
        p = np.mat([[1,1],[1,0]])
        ret = matPow(p,n)

        return ret.tolist()[0][0]
