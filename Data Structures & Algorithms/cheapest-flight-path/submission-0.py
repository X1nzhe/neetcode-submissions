class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, p in flights:
            adj[u].append((v,p))
        
        heap = [ (0, src, 0)] # cost, current node, flights taken
        best = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost
            if stops > k:
                continue
            if node in best and best[node] <= stops:
                continue
            best[node] = stops

            for nei, price in adj[node]:
                heapq.heappush(heap, (cost+price, nei, stops+1))
        
        return -1