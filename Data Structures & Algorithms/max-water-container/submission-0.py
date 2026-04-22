class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float('-inf')

        left, right = 0, len(heights)-1

        while left < right:
            height = min(heights[left], heights[right])
            res = max(res, height * (right-left))
            
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                left += 1
        
        return res