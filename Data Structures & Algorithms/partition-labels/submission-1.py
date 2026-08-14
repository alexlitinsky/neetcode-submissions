class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        labels = {}

        res = []

        for i, c in enumerate(s):
            labels[c] = i

        idx = 0
        start = -1
        for i in range(len(s)):
            idx = max(idx, labels[s[i]])
            if i >= idx:
                res.append(idx - start)
                start = i
        
        return res



        