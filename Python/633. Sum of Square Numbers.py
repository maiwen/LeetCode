# -*- coding: utf-8 -*-
"""
Created on 2018/7/4 17:04

@author: vincent
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""
import math
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            if (i * i + j * j) == c:
                return True
            elif (i * i + j * j) >= c:
                j -= 1
            elif (i * i + j * j) <= c:
                i += 1
        return False