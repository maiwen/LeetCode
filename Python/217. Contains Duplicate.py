# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 17:05

@author: vincent
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = dict()

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
            d[nums[i]] += 1
            if d[nums[i]] > 1:
                return True
        return False