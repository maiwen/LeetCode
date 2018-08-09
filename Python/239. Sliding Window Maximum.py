# -*- coding: utf-8 -*-
"""
Created on 2018/8/9 10:52

@author: vincent

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?


"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        if not nums or n < k:
            return []
        for i in range(n):
            if i+k < n+1:
                result.append(max(nums[i:i+k]))
            else:
                break
        return result

from collections import *
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        result = []
        for i,num in enumerate(nums):
            while d and num > nums[d[-1]]:
                d.pop()
            d.append(i)
            if d[0] <= i-k:
                d.popleft()
            if i >= k - 1:
                result.append(nums[d[0]])
        return result