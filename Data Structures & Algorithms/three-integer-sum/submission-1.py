class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -num
            
            left, right = i+1, len(nums)-1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif two_sum > target:
                    right -= 1
                else: left += 1

        return res
                




        