# -*- coding: utf-8 -*-
"""
Created on 2018/7/9 17:26

@author: vincent
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""


class Solution:

    def subrob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [[0] for i in range(n)]
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            if i == 1:
                dp[i] = max(nums[i - 1], nums[i])
            if i == 2:
                dp[i] = max(nums[i - 1], nums[i] + nums[i - 2])
            if i > 2:
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        return max(dp[n - 1], dp[n - 2])

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.subrob(nums[:-1]), self.subrob(nums[1:]))