# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, subsum = nums[0], 0
        for num in nums:
            subsum += num
            result = max(result, subsum)
            if subsum < 0: 
                subsum = 0
        return result
