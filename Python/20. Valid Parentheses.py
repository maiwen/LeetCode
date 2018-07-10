# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 16:14

@author: vincent
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bra = {')':'(', '}':'{', ']':'['}
        left = ['(','{','[']
        right = [')','}',']']
        if len(s) == 0 or len(s) == 1 or s[0] in right:
            return False
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif s[i] in right:
                if stack:
                    if stack[-1] == bra[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False