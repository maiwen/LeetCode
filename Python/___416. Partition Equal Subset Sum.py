# -*- coding: utf-8 -*-
"""
Created on 2018/7/16 14:46

@author: vincent
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumv = sum(nums)
        if sumv % 2 != 0:
            return False
        n = len(nums)
        W = int(sumv / 2)
        dp = [False] * (W+1)
        dp[0] = True
        nums = sorted(nums)
        for num in nums:
            for i in range(W,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        return dp[W]

    def helper(self, nums, start, target):  # Here path is not needed
        if target < 0:
            return False
        elif target == 0:
            return True
        for i in range(start, len(nums)):
            if self.helper(nums, i + 1, target - nums[i]):
                return True
        return False

    def canPartition1(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        nums.sort(reverse=True)
        if nums[0] > total / 2:
            return False
        return self.helper(nums, 0, total / 2)