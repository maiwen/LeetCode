# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 10:25

@author: vincent
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        count = 0
        dp = [0] * n
        for i in range(2,n):
            if dp[i-1] > 0:
                if A[i] - A[i-1] == A[i-1] - A[i-2]:
                    count += (dp[i-1]-1)
                    dp[i] = dp[i-1]+1
            else:
                if A[i] - A[i-1] == A[i-1] - A[i-2]:
                    count += 1
                    dp[i] = 3
        return count

    def numberOfArithmeticSlices1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        res = [0 for _ in range(n)]
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                res[i] = res[i - 1] + 1
        return sum(res)