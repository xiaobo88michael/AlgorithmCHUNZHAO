class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def my_pow(x,n):
            if n==0:
                return 1
            
            y = my_pow(x,n/2)
            if n%2==0:
                return y*y
            else:
                return y*y*x
        if n<0:
            return 1/my_pow(x,-n)
        
        return my_pow(x,n)
