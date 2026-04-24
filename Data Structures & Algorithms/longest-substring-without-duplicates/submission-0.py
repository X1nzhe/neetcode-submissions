class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_set = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in chars_set:
                chars_set.remove(s[l])
                l += 1
            chars_set.add(s[r])
            res = max(res, r-l+1)
        return res

        