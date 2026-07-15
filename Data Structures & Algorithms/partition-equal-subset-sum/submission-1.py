from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        target = total // 2
        
        @cache
        def dfs(i, target):
            if target == 0:
                return True
            if i == len(nums) or target < 0:
                return False

            if dfs(i+1,target):
                return True
            
            return dfs(i+1, target - nums[i])
        
        return dfs(0, target)

            
            
            
            
        