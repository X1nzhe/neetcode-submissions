from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
        
        tails = []

        for num in nums:
            index = bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num
        
        return len(tails)