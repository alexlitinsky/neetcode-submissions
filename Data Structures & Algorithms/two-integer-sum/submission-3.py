class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        intMap = defaultdict(int)
        for i, n in enumerate(nums):
            if target - n in intMap:
                return [intMap[target - n], i]
            intMap[n] = i
        