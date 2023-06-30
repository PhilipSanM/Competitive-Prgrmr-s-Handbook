# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 121. Best Time to Buy and Sell Stock -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: June - 30 - 2023
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# ====================================================================

# Sliding window
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        # Sliding
        buy = prices[0]
        for sell_price in prices:
            if sell_price > buy:
                max_profit = max(max_profit, sell_price - buy)
            else:
                buy = sell_price


        return max_profit