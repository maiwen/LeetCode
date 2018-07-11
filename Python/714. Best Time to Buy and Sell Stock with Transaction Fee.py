# -*- coding: utf-8 -*-
"""
Created on 2018/7/11 15:28

@author: vincent

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) < 2: return 0
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, prices[1] - prices[0] - fee)
        for i in range(2, n):
            buy[i] = max(sell[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i] - fee, sell[i - 1])

        return sell[n - 1]