class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, nums):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start+1, nums)
                nums[start], nums[i] = nums[i], nums[start]
        
        dfs(0, nums)
        return res
        