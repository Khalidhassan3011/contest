class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, lowest = 0, None

        for price in prices:
            if lowest is None or price < lowest:
                lowest = price
            elif price - lowest > profit:
                profit = price - lowest
        return profit
