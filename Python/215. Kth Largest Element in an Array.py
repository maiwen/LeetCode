# -*- coding: utf-8 -*-
"""
Created on 2018/7/6 16:34

@author: vincent
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
"""
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for num in nums:
            heapq.heappush(h,-num)
        for i in range(k):
            result = heapq.heappop(h)
        return -result
