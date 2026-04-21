class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i, num in enumerate(nums):
            target = -num
            
            left, right = i+1, len(nums)-1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    curr = (num, nums[left], nums[right])
                    res.add(curr)
                    left += 1
                    right -= 1
                elif two_sum > target:
                    right -= 1
                else: left += 1

        return [list(t) for t in res]
                




        