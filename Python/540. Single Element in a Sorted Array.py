# -*- coding: utf-8 -*-
"""
Created on 2018/7/9 9:34

@author: vincent

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            lSize = mid - l

            '''
            If the value is between 2 values
            then that is the single value
            '''
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                return nums[mid]

            """            
            Compare against left side of mid
            The idea is to ensure that odd number of elements remain
            on the side we eventually consider next
            If the size on either side of mid is even, then
            set r as mid to ensure odd number of elements,
            Else set l as mid + 1
            Repeat the same for the right side of mid
            """
            if nums[mid - 1] == nums[mid]:
                if lSize % 2 == 0:
                    r = mid
                else:
                    l = mid + 1

            else:
                if nums[mid] == nums[mid + 1]:
                    if lSize % 2 == 0:
                        l = mid
                    else:
                        r = mid - 1

        """
        In the end we will be left with just one element
        which is going to be answer
        """
        return nums[l]