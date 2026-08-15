class Solution:
    def isPalindrome(self, s: str) -> bool:

        lst = []

        for c in s:
            if c.isalnum():
                lst.append(c.lower())
        
        l, r = 0, len(lst) - 1

        while l <= r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        
        return True

        