class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        self.prices = prices
        n = len(prices)
        max_profit = 0
        mini = float("inf")

        for i in range(0,n):
            mini = min(mini,prices[i])
            max_profit = max(max_profit,prices[i]-mini)

        return max_profit