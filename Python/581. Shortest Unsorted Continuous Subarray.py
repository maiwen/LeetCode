# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 17:03

@author: vincent

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, sorts = len(nums), sorted(nums)
        if nums == sorts: return 0
        l, r = min(i for i in range(n) if nums[i] != sorts[i]), max(i for i in range(n) if nums[i] != sorts[i])
        return r - l + 1

    def findUnsortedSubarray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        s = e = -1
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                if s == -1: s = i
                e = i
        return e - s + 1 if e != s else 0