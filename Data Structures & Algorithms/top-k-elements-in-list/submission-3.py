class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        topk = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        for n, f in freq.items():
            topk[f].append(n)
        
        res = []

        for i in range(len(topk) -1, -1, -1):
            for val in topk[i]:
                res.append(val)
                if len(res) == k:
                    return res
                    