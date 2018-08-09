# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:50:34 2018

@author: Administrator

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

埃氏筛法
素数就是除了1和本身之外没有其他的约数，所以有约数的都不是素数。

思路：
先去掉2的倍数，再去掉3的倍数，再去掉4的倍数，……依此类推，最后剩下的就是素数。 
如求100以内的素数，我们只要到去掉Math.aqrt(100)的倍数就可以了，这是因为10的2倍已经被2的倍数去掉了，
10的3倍已经被3的倍数去掉了，所以到10的时候只剩下10的10倍以上的素数还存在。 
同样的原因，我们在去掉3的倍数的时候，只要从3的3倍开始去掉就好了，因为3的2倍已经被2的倍数去掉了。
"""
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
