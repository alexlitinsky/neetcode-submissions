class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if n == 0: return 1
            if n == 1: return x

            extra = x if n % 2 == 1 else 1

            return helper(x, n // 2) * helper(x, n // 2) * extra


        return helper(x, n) if n >= 0 else 1 / helper(x, -1 * n)
        