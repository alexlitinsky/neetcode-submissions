class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c) - ord("a")] += 1
            key = tuple(word)
            res[key].append(s)
        
        return list(res.values())


        