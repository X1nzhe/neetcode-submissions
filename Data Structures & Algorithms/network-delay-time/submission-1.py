class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        distance = {node: float('inf') for node in range(1, n+1)}
        distance[k] = 0
        heap = [(0, k)]

        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distance[node]:
                continue
            for nei, w in adj[node]:
                new_dist = dist+ w

                if new_dist < distance[nei]:
                    distance[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))
        res = max(distance.values())
        return res if res != float('inf') else -1
                