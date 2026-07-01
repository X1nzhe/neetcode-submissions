class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2**31-1
        directions = [
            [1,0], [-1,0],
            [0,1], [0,-1]
        ]
        def bfs(r, c):
            q = deque([(r,c)])
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            visited[r][c] = True
            steps = 0

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0<=nr < rows and 0<= nc < cols and not visited[nr][nc] and grid[nr][nc] != -1):
                            visited[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)