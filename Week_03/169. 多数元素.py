class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        candy = 0
        for num in nums:
            if count==0:
                candy = num
            
            if candy==num:
                count+=1
            else:
                count-=1
        
        return candy
