# -*- coding: utf-8 -*-
"""
Created on 2018/7/9 18:35

@author: vincent

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

"""


class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.dp = self.getDp(nums)

    def sumRange(self, i, j):
        return self.dp[j] - self.dp[i] + self.nums[i]

    def getDp(self, nums):
        dp = [0] * len(nums)
        if nums != []:
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                dp[i] = dp[i - 1] + nums[i]
        return dp

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)