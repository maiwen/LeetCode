# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 17:07

@author: vincent

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

"""
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseString1(self, s):
        chars, lo, hi = list(s), 0, len(s) - 1
        while lo < hi:
            chars[lo], chars[hi] = chars[hi], chars[lo]
            lo += 1
            hi -= 1
        return ''.join(chars)