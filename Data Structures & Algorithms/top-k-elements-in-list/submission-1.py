class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums_count = Counter(nums)

        # return [x for x, _ in nums_count.most_common(k)]

        nums_dict = {} # num : count

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        nums_dict_list = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)

        return [x for x, _ in nums_dict_list[:k]]





