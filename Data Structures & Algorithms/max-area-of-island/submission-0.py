class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        directions = [
            [1,0], [-1, 0], 
            [0, 1], [0, -1]
        ]

        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            curr_area = 1
            for dr, dc in directions:
                curr_area += dfs(r+dr, c+dc)
            
            return curr_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area      


        