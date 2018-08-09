# Given an integer array, find three numbers whose product is maximum and output the maximum product.

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] < 0 and nums[1] < 0:
            if nums[0] * nums[1] * nums[-1] > nums[-1] * nums[-2] * nums[-3]:
                return nums[0] * nums[1] * nums[-1]
            else:
                return nums[-1] * nums[-2] * nums[-3]
        return nums[-1] * nums[-2] * nums[-3]
    
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        a,b=heapq.nlargest(3,nums),heapq.nsmallest(2,nums)
        return max(a[0]*a[1]*a[2],b[0]*b[1]*a[0])
      
