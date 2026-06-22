class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return
            seen = set()
            for i in range(start, len(candidates)):
                if candidates[i] in seen:
                    continue
                seen.add(candidates[i])
                path.append(candidates[i])
                dfs(i+1, path, remaining - candidates[i])
                path.pop()
        
        dfs(0, [], target)

        return res