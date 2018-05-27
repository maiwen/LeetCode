# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        maxsub , sub = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                sub += 1
            else:
                if sub > maxsub:
                    maxsub = sub
                sub = 1
        if sub > maxsub:
            maxsub = sub
        return maxsub
