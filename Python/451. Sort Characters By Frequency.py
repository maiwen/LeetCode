# -*- coding: utf-8 -*-
"""
Created on 2018/7/6 17:03

@author: vincent

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        fre = {}
        for c in s:
            if c in fre:
                fre[c] += 1
            else:
                fre[c] = 1
        bucket = [[] for _ in range(len(s) + 1)]

        for key, val in fre.items():
            for i in range(val):
                bucket[val].append(key)
        result = []
        for b in reversed(bucket):
            for i in b:
                result.append(i)
        return ''.join(result)