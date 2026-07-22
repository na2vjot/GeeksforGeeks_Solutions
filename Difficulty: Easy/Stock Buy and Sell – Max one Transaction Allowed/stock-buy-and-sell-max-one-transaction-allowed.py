class Solution:
    def maxProfit(self, prices):
        # code here
        max_prof = 0
        min_price = float('inf')
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_prof:
                max_prof = price - min_price
                
        return max_prof