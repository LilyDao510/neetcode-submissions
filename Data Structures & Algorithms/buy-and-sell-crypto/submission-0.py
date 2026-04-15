class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0,1
        l = len(prices)
        max_profit = 0
        while s < l:
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                max_profit = max(max_profit,profit)
            else:
                b = s
            s +=1
        return max_profit

        