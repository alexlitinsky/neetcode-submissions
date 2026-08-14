class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()

        while True:
            s = str(n)
            newN = 0
            for c in s:
                newN += int(c) ** 2
            if newN == 1: return True
            if newN in visit: return False
            visit.add(newN)

            n = newN



        