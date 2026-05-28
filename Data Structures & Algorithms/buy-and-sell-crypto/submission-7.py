class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of maxProfit

        i = 0
        j = 0
        n = len(prices)
        maxProfit  = 0

        while i <= j and j < n:
            profit = prices[j] - prices[i]
            
            # if profit is less than 0, it means we've found a new lower price
            # set i to new lower price i.e j
            if profit < 0:
                i = j

            maxProfit = max(maxProfit, profit)

            j += 1

        return maxProfit
    