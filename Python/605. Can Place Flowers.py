# -*- coding: utf-8 -*-
"""
Created on 2018/7/4 16:05

@author: vincent

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        if len(flowerbed) >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
        if flowerbed == [0]:
            n -= 1
            flowerbed[0] = 1
        while i + 2 < len(flowerbed):
            if flowerbed[i] == 1:
                i += 1
            else:
                if flowerbed[i + 1] == 0 and flowerbed[i + 2] == 0:
                    flowerbed[i + 1] = 1
                    n -= 1
                i += 2
        if len(flowerbed) >= 3 and flowerbed[-3] == 1 and flowerbed[-2] == 0 and flowerbed[-1] == 0:
            n -= 1

        return (n <= 0)

    def canPlaceFlowers1(self, a, n):
        if n == 0: return True
        a = [0] + a + [0]
        for i in range(1, len(a) - 1):
            if a[i - 1] == a[i] == a[i + 1] == 0:
                a[i] = 1
                n -= 1
                if n == 0: return True

        return False

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,0,1],2))