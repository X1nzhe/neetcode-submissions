from functools import cache

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_sum = max_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum+num)
            max_sum = max(cur_sum, max_sum)
        return max_sum
        

        