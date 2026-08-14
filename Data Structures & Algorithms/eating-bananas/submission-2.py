class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        k = max(piles)

        while left <= right:
            rate = (left + right) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / rate)
            if time <= h:
                k = min(k, rate)
                right = rate - 1
            else:
                left = rate + 1

        return k