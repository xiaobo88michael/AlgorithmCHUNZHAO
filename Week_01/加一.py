class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)

        if digits==[]:
            return []
        
        for i in range(n-1,-1,-1):
            digits[i]=digits[i]+1
            if digits[i]%10==0:
                digits[i]=0
            else:
                return digits
        
        if digits[0]%10==0:
            digits=[1]+digits
        
        return digits
