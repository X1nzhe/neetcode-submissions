class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visited = set()
        min_heap = [(0,0)] # cost, node

        while len(visited) < len(points):
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            res += cost
            for v in range(len(points)):
                if v not in visited:
                    d = abs(points[u][0] - points[v][0])+ abs(points[u][1]-points[v][1])
                    heapq.heappush(min_heap, (d,v))
        return res


