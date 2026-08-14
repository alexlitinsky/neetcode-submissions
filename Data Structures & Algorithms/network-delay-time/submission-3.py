class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append([v, w]) 

        visited = set()
        t = 0
        minH = [(0, k)]

        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visited: continue
            visited.add(n1)
            t = w1


            for n2, w2 in adj[n1]:
                if n2 in visited: continue
                heapq.heappush(minH, (w1 + w2, n2))

        
        return t if len(visited) == n else -1

        