from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(idx, value):
            if idx == len(coins) or value > amount:
                return 0
            if value == amount:
                return 1
            return dfs(idx, value+coins[idx]) + dfs(idx+1, value)
        
        return dfs(0, 0)
            
