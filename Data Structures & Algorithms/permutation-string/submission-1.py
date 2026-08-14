class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        res = Counter(s1)
        cur = Counter(s2[:len(s1)])
        l = 0

        for r in range(len(s1), len(s2)):
            if cur == res:
                return True

            cur[s2[l]] -= 1
            if cur[s2[l]] == 0:
                cur.pop(s2[l])
            l += 1

            if s2[r] not in cur:
                cur[s2[r]] = 0
            cur[s2[r]] += 1
            
        return cur == res

        # le
        