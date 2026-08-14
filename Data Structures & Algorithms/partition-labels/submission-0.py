class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        res = []
        sMap = Counter(s)

        count = set()

        start = 0

        for i in range(len(s)):
            sMap[s[i]] -= 1
            if sMap[s[i]] > 0:
                count.add(s[i])
            elif sMap[s[i]] == 0:
                sMap.pop(s[i])
                count.discard(s[i])
                if not count:
                    res.append(i - start + 1)
                    start = i + 1


        return res
        