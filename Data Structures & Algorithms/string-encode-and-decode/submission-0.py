class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # 10#asdasdasdas
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            L = int(s[i:j])
            res.append(s[j + 1 : j + 1 + L])

            i = j + 1 + L
        
        return res
