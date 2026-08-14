class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY: return False

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
                rank[rootX] += rank[rootY]
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
                rank[rootY] += rank[rootX]
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        