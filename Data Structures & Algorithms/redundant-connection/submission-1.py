class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))

        # find root node
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False

            parent[root_u] = root_v
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

