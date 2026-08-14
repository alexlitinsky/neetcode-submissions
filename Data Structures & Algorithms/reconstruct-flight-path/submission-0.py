class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        edges = defaultdict(list)

        for src, dst in tickets:
            edges[src].append(dst)
        
        for k, v in edges.items():
            edges[k].sort(reverse=True)
        
        res = []

        def dfs(src):
            while edges[src]:
                nei = edges[src].pop()
                dfs(nei)
            res.append(src)
        

        dfs("JFK") 
        return res[::-1]
        
        