# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 16:57

@author: vincent
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i += 1
            else:
                break
        return str1[:i]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            return reduce(self.lcp, strs)
        else:
            return ''

    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_len = min([len(x) for x in strs])
        i, out = 0, ''
        while i < min_len:
            tmp = [x[i] for x in strs]
            if len(set(tmp)) == 1:
                out = out + tmp[0]
            else:
                break
            i += 1
        return out