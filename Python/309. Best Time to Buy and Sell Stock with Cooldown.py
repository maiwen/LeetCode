# -*- coding: utf-8 -*-
"""
Created on 2018/7/11 15:12

@author: vincent
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

设sell[i]  第i天手上有股票（或者卖或者什么都不做），能获得的最大利润

buy[i] 第i天手上无股票（或者买或者什么都不做），能获得的最大利润

所以，显然有状态转移方程

buy[i] = max(buy[i-1] , sell[i-2] – prices[i])
sell[i] = max(sell[i-1], buy[i-1] + prices[i])
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2: return 0
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, prices[1] - prices[0])
        for i in range(2, n):
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])

        return sell[n - 1]