class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2: return [strs]

        strs_dict = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            strs_dict[key].append(s)
        return list(strs_dict.values())
