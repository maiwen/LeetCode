# -*- coding: utf-8 -*-
"""
Created on 2018/7/9 9:33

@author: vincent

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"
"""
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, h = 0, len(letters)
        while l < h:
            m = (l+h) / 2
            if letters[m] > target:
                h = m
            else:
                l = m + 1
        return letters[l % len(letters) ]