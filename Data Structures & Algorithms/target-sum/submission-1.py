from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(i, value):
            if i == len(nums):
                return 1 if value == target else 0
                
            return dfs(i+1, value+nums[i]) + dfs(i+1, value-nums[i])
        
        return dfs(0, 0)
            