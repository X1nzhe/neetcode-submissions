class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        n = len(s)

        for i in range(n):
            for l , r in ((i,i), (i,i+1)):
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                l, r = l+1, r-1

                if r-l+1 > len(res):
                    res = s[l:r+1]
        
        return res

        