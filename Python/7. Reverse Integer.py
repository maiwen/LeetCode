# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 16:51

@author: vincent
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483648 or x < -2147483648:
            return 0
        num = str(x)
        neg = False
        result = ''
        s = []
        list = []
        for i in num:
            s.append(i)
        if s[0] == '-':
            del s[0]
            neg = True
        size = len(s)
        while s[size-1] == 0:
            del s[size-1]
        if neg:
            global result
            result = '-'
        for i in range(len(s)):
            result = result + s[len(s)-i-1]
        rev = int(result)
        if rev > 2147483648 or rev < -2147483648:
            return 0
        else:
            return rev

    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """

        negative = x < 0
        if negative:
            x *= -1

        digits = list(str(x))
        digits.reverse()
        reversed = "".join(digits)
        output = int(reversed)

        if negative:
            output *= -1

        if output > 2147483647 or output < -2147483648:
            return 0

        return output