from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = []
        min_price = 10**4 + 1
        max_price = -1
        max_profit = 0
        # flag for whether price is increasing
        increasing = False
        for price in prices:
            # price decreasing, update minimum price
            if price <= min_price and not increasing:
                min_price = price
            # else if previous trend was decreasing and price greater now, update maximum price
            elif (price > min_price and not increasing) or (price > max_price and increasing):
                increasing = True
                max_price = max(price, max_price)
            # If previous trend was increasing and price smaller now, trend is now decreasing
            # Update max profit and reset maximum price (price is less than max price so need not consider this)
            elif price < max_price and increasing:
                increasing = False
                max_profit = max(max_profit, max_price - min_price)
                max_price = -1
                min_price = min(min_price, price)

        return max(max_profit, max_price - min_price) 