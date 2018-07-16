# -*- coding: utf-8 -*-
"""
Created on 2018/7/13 10:12

@author: vincent
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""
class Solution:
    def minDistance(self, A, B):
        M, N = len(A), len(B)
        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(M):
            dp[i][-1] = M-i
        for j in range(N):
            dp[-1][j] = N-j

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]