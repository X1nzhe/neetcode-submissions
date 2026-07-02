class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        directions = [
            [1, 0], [-1,0],
            [0,1],[0,-1]
        ]

        def dfs(r,c, reacable_set):
            reacable_set.add((r,c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<= nr < rows and 0<=nc < cols and (nr, nc) not in reacable_set and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reacable_set)
        
        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows - 1, c, atlantic_reachable)
        
        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols-1, atlantic_reachable)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    res.append([r,c])
        return res




        