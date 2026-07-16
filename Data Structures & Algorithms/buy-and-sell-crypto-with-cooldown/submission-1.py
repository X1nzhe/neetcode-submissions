from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, holding):# if holding a coin at ith day
            if i >= len(prices):
                return 0
            if holding: # if have a coin

                # option 1: keep the coin
                keep = dfs(i+1, True)

                # option 2: sell
                sell = prices[i] + dfs(i+2, False)
                return max(keep, sell)
            else: # if not have a coin
                # skip or buy a coin
                skip = dfs(i+1, False)
                buy = dfs(i+1, True) - prices[i]
                return max(skip, buy)

        return dfs(0, False)




            
        