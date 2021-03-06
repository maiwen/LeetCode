# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 16:55

@author: vincent

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
class Solution(object):

    def romanToInt(self, s):

        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Should try to deal with M, then D, then C, then L, then X, then V, then I

        # I II III IV V VI VII VIII IX
        # X XX XXX XL L LX LXX LXXX XC
        # C CC CCC CD D DC DCC DCCC CM
        # M

        # We basically have four sections of each number that we must evaluate; 1000s, 100s, 10s

        # 1. Break number into its respective segments
        # 2. Evaluate what each segment represents

        total = 0
        prev = 1000
        for letter in s:
            cur = roman[letter]
            if prev < cur:
                total -= prev * 2
            total += cur
            prev = cur

        return total