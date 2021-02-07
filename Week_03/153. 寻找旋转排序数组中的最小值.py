class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        low ,high = 0,n-1
        if n==1 or nums[0]<=nums[n-1]:
            return nums[0]
        

        while low<=high:
            
            mid = (low+high)/2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid-1]>nums[mid]:
                return nums[mid]

            if nums[mid]>nums[0]:
                low = mid+1
            else:
                high = mid-1
