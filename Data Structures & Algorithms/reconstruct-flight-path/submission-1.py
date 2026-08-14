class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        flights = defaultdict(list)

        for src, dst in tickets:
            flights[src].append(dst)
            flights[src].sort()
            flights[src].reverse()
        
 
        def dfs(src):
            res = []

            while flights[src]:
                dst = flights[src].pop()
                tmp = dfs(dst)
                res.extend(tmp)
            
            res.append(src)

            return res

        



        return dfs("JFK")[::-1]
        