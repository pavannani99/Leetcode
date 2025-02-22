class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_current = max_global = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]  # Daily profit/loss
            max_current = max(0, max_current + diff)  # Reset if negative
            max_global = max(max_global, max_current)  # Update max profit

        return max_global
