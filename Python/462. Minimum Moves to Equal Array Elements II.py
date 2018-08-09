# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 19:25:37 2018

@author: Administrator

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums)-1
        nums = sorted(nums)
        move = 0
        while l <= h:
            move += nums[h] - nums[l]
            l += 1
            h -= 1
        return move