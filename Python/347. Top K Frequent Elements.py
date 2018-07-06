# -*- coding: utf-8 -*-
"""
Created on 2018/7/6 16:54

@author: vincent

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fre = {}
        for num in nums:
            if num in fre:
                fre[num] += 1
            else:
                fre[num] = 1
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, val in fre.items():
            bucket[val].append(key)
        result = []
        for b in reversed(bucket):
            for i in b:
                result.append(i)
                if len(result) == k:
                    return result