# -*- coding: utf-8 -*-
"""
Created on 2018/7/11 10:31

@author: vincent
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""
class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda x:x[0])
        n = len(pairs)
        if n < 2:
            return n
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def findLongestChain1(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        last_end = -0x7FFFFFFF
        pairs.sort(key=lambda x: x[1])

        count = 0
        for pair in pairs:
            if pair[0] > last_end:
                last_end = pair[1]
                count += 1
        return count