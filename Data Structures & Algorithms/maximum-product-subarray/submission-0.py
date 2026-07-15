class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for num in nums[1:]:
            prev_max = curr_max
            prev_min = curr_min

            curr_max = max(
                num,
                prev_max * num,
                prev_min * num
            )
            curr_min = min(
                num,
                prev_max * num,
                prev_min * num
            )
            res = max(res, curr_max)
        
        return res
        
        