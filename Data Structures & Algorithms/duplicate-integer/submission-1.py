class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dupl = set()

        for n in nums:
            if n in dupl:
                return True
            dupl.add(n)
        
        return False
        