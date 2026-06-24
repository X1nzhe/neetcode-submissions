class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):
                t = s[start:i+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(i+1, path)
                    path.pop()

        dfs(0, [])
        return res

        