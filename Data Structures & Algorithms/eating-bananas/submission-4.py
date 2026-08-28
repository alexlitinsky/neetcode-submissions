class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        minPiles = max(piles)

        while l < r:
            m = (l + r) // 2
            est = 0
            for p in piles: est += math.ceil(p / m)
            if est <= h:
                minPiles = min(minPiles, m)
                r = m
            else:
                l = m + 1
        
        return minPiles


        

        