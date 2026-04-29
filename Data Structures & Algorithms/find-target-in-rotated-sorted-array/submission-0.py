class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1 find index of the minimum number in the array
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l) // 2
            if nums[r] < nums[mid]:
                l = mid + 1 # pivot in right part
            else:
                r = mid
        
        pivot = l
        # Step 2 find which part includes target
        l, r = 0, len(nums) - 1
        if nums[pivot] <= target and target <= nums[r]: # target in the right part
            l = pivot
        else: 
            r = pivot - 1 # target in the left part
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # target in the right part
                l = mid+1
            else:
                r = mid-1
        
        return -1

        






                
        