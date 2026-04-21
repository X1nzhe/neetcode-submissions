class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 2:
            return [1, 2]

        left, right = 0, n-1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left+1, right+1]
            if  two_sum > target:
                right -= 1
            else:
                left += 1
            
        
        