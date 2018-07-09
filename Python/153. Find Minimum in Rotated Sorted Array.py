# -*- coding: utf-8 -*-
"""
Created on 2018/7/9 10:02

@author: vincent
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
class Solution(object):
    def findMin(self, a):
        # T(n) = O(log n)
        # S(n) = O(1)
        lo, hi = 0, len(a)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if a[mid] > a[hi]:
                lo = mid+1
            elif mid == 0 or (mid-1 >= 0 and a[mid-1] > a[mid]):
                return a[mid]
            else:
                hi = mid-1
        raise RuntimeError