class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        nums_set = set(nums)
        starts = defaultdict(list)
        for num in nums_set:
            if num - 1 not in nums_set:
                starts[num].append(num)

        for start in starts:
            current = start
            while current + 1 in nums_set:
                starts[start].append(current+1)
                current += 1
        
        return len(max(starts.values(), key=len))


        