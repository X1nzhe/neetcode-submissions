class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 2:
            return [1, 2]

        left, right = 0, n-1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
                continue
            if numbers[left] + numbers[right] < target:
                left += 1
                continue
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
        
        