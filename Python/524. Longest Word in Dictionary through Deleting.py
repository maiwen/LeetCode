# -*- coding: utf-8 -*-
"""
Created on 2018/7/4 18:38

@author: vincent

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""

class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d = sorted(d)
        d = sorted(d, key=len, reverse=True)
        for c in d:
            tmp_s = s
            index = 0
            while index < len(c):
                if c[index] not in tmp_s:
                    break
                tmp_s = tmp_s[tmp_s.index(c[index]) + 1:]
                index += 1
            if index == len(c):
                return c
        return ''