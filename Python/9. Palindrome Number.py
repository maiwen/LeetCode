# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 16:53

@author: vincent
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digit = 1
        while(x/digit >= 10):
            digit *= 10
        while(x != 0):
            left = x / digit
            right = x % 10
            if left != right:
                return False
            x = (x % digit) / 10
            digit /= 100
        return True

    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        original_x = x
        reversed = 0
        while x > 0:
            reversed *= 10
            reversed += x % 10
            x //= 10
        return reversed == original_x