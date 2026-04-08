# Last updated: 4/8/2026, 9:14:19 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_buy = prices[0]
        max_sell = 0
        for i in prices:
            min_buy = min(min_buy, i)
            max_sell = max(max_sell, i - min_buy)
        return max_sell