class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        distances = [float('inf')] * n
        distances[src] = 0 

        for _ in range(k + 1):
            distances_copy = distances[:]
            for u, v, cost in flights:
                if distances[u] != float('inf') and distances[u] + cost < distances_copy[v]:
                    distances_copy[v] = distances[u] + cost
            print(distances_copy)
            distances = distances_copy
        
        print(distances)
        return distances[dst] if distances[dst] != float('inf') else -1