class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if not nums:
            return -1
        low,high = 0,n-1
        
        while low<=high:
            mid = (low+high)/2
            if nums[mid]==target:
                return mid

            if nums[0]<=nums[mid]:
                if nums[0]<=target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid]<target<=nums[n-1]:
                    low = mid+1
                else:
                    high = mid-1
        
        return -1
