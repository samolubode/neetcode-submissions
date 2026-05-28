class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        j = 0
        n = len(prices)
        maxProfit  = 0

        while i <= j and j < n: # [3,4,1]
            profit = prices[j] - prices[i]
            if profit < 0:
                i = j

            maxProfit = max(maxProfit, profit)

            j += 1

        return maxProfit
    