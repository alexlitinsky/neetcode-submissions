class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        tx, ty, tz = target
        best = [0, 0, 0]

        for a, b, c in triplets:
            if a <= tx and b <= ty and c <= tz:
                best[0] = max(best[0], a)
                best[1] = max(best[1], b)
                best[2] = max(best[2], c)


        return best == target
        