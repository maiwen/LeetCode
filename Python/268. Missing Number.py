class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        
        if nums[0] != 0:
            return 0
        for i in range(len(nums)): 
            if i != nums[i]:
                return i
