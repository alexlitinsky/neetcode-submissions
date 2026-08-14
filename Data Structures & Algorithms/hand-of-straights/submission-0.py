class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        count = Counter(hand)

        for x in sorted(count):
            k = count[x]
            if k == 0: continue
            for i in range(groupSize):
                if count[x + i] < k: return False
                count[x + i] -= k
        return True
        