class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(houses: List[int]):
            prev, curr = 0, 0
            for h in houses:
                prev, curr = curr, max(curr, prev+h)
            return curr
        
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))
        