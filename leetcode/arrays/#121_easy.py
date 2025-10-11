'''
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        will fail as time complexity is 0(n^2)
        '''
        max = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j]-prices[i] > max:
                    max= prices[j]-prices[i]

        return max
    
    def max_profit(self, prices: List[int]) -> int:
        '''
        Optimal solution with 0(n) time complexity
        '''
        min = prices[0]
        profit = 0
        for price in prices:
            if price < min:
                min = price
            if price-min > profit:
                profit = price-min
        return profit