class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_fruit = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [
            [1, 0], [-1,0],
            [0, 1], [0, -1]
        ]
        minutes = 0
        while q and fresh_fruit:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<= nr < rows and 0<=nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh_fruit -= 1
            minutes += 1
        return  minutes if  not fresh_fruit else -1
