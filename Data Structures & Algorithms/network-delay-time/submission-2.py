class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i : [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append([v, w]) 

        visited = set()
        res = 0
        minH = [(0, k)]

        while minH and len(visited) != n:
            t, v = heapq.heappop(minH)
            if v in visited: continue
            visited.add(v)
            if len(visited) == n:
                return t
            # print(t, v, minH, visited)

            for nei, newT in adj[v]:
                if nei in visited: continue
                heapq.heappush(minH, (t + newT, nei))

            res += 1
        
        return res if len(visited) == n else -1

        