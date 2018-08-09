# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 18:27:13 2018

@author: Administrator

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.


"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        subnum = 1
        while num > 0:
            num -= subnum
            subnum += 2
        return num == 0