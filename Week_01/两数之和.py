class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums)
        dic = {}

        for i in range(n):
            if target-nums[i]  in dic:
                return [dic[target-nums[i]],i]
            dic[nums[i]]=i 
        
        return []
