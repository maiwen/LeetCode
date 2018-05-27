# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) == 1:
            return 0
        maxnum = max(nums)
        maxindex = nums.index(maxnum)
        del nums[maxindex]
        if max(nums) == 0 or maxnum / max(nums) >= 2:
            return maxindex
        else:
            return -1
