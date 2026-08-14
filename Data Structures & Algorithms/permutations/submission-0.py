class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for n in nums:
                if n in curr:
                    continue
                curr.append(n)
                backtrack()
                curr.pop()
            

        backtrack()
        return res
        