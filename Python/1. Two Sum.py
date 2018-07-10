# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 16:50

@author: vincent
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return 0
        dictnum = {}
        for i in range(len(nums)):
            complete = target - nums[i]
            if complete in dictnum:
                return dictnum[complete], i
            else:
                dictnum[nums[i]] = i