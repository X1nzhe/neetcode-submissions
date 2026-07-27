from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(idx1, idx2, idx3):
            if idx3 == len(s3):
                return (idx1 == len(s1)) and (idx2 == len(s2)) # fully matched
            if idx1 < len(s1) and s1[idx1] == s3[idx3]:
                if dfs(idx1+1, idx2, idx3+1):
                    return True
            if idx2 < len(s2) and s2[idx2] == s3[idx3]:
                if dfs(idx1, idx2+1, idx3+1):
                    return True
            return False

        return dfs(0, 0, 0)


            