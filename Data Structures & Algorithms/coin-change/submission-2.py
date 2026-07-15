from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def dfs(amount):
            if amount == 0:
                return 0
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res

        min_coins = dfs(amount)
        return -1 if min_coins == float('inf') else min_coins

        