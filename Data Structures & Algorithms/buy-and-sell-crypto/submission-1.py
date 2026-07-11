class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0 
        minPrice = prices[0]

        for price in prices: 
            maxP = max(maxP, price - minPrice)
            minPrice = min(minPrice, price)

        return maxP 
        


        