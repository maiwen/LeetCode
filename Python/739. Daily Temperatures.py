# -*- coding: utf-8 -*-
"""
Created on 2018/7/16 15:22

@author: vincent

Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)
        stack.append(0)
        for i, v in enumerate(temperatures):
            while len(stack) !=0 and v > temperatures[stack[-1]]:
                pre = stack.pop()
                result[pre] = i-pre
            stack.append(i)
        return result

    def dailyTemperatures1(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # clever solution
        # start backwards from the array
        # first element is 0
        # supporse we have found the correct days from position j+1 to the last
        # consider j. two possibilities appear:
        #   temp[j] < temp[j+1] -> days[j] = 1
        #   temp[j] >= temp[j+1] -> we can skip to j+1 + days[j+1], since previous days are colder anyway
        n = len(temperatures)
        days = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while True:
                if temperatures[i] < temperatures[j]:
                    days[i] = j - i
                    break
                elif days[j] == 0:
                    break
                j += days[j]

        return days