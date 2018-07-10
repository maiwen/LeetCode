# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 17:09

@author: vincent
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if ' ' not in s:
            return self.reverseString(s)
        pre = 0
        result = ''
        for i in range(len(s)):
            if s[i] == ' ':
                result += self.reverseString(s[pre:i])
                result += ' '
                pre = i + 1
            if i == len(s) - 1:
                result += self.reverseString(s[pre:i + 1])

        return result

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Check whether the input string is None or empty
        if not s:
            return ''

        parts = s.split()
        for i, part in enumerate(parts):
            parts[i] = part[::-1]
        return ' '.join(parts)