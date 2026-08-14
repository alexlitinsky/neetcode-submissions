class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = Counter(nums)
        order = [[] for i in range(len(nums) + 1)]

        for num, freq in freqs.items():
            order[freq].append(num)
        
        res = []

        for i in range(len(order) - 1, -1, -1):
            for j in range(len(order[i])):
                res.append(order[i][j])
                k -= 1
                if not k:
                    return res

        
        


        