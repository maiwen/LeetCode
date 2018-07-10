# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 17:01

@author: vincent
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Seen this question in a real interview before?

"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '' and needle =='':
            return 0
        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+length] == needle:
                return i
        return -1

    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1