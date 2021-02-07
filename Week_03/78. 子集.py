class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        for i in nums:
            res = res+([num+[i] for num in res])
        
        return res
    
