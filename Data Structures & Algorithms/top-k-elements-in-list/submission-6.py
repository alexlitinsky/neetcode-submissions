class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqList = [[] for _ in range(len(nums) + 2)]
        for n, f in counts.items():
            freqList[f].append(n)
        
        res = []

        for i in range(len(freqList) -1, -1, -1):
            while freqList[i]:
                val = freqList[i].pop()
                res.append(val)
            if len(res) == k:
                return res


        