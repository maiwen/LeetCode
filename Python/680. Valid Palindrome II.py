# -*- coding: utf-8 -*-
"""
Created on 2018/7/4 17:33

@author: vincent
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[::-1]==s:
            return True
        i=0
        j=len(s)-1
        while(i<j):
            if s[i] != s[j]:
                sA=s[:i]+s[i+1:]
                sB=s[:j]+s[j+1:]
                if sA==sA[::-1] or sB==sB[::-1]:
                    return True
                else:
                    return False
            i+=1
            j-=1