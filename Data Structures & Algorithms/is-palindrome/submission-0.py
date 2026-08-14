class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphanum = ''.join(c.lower() for c in s if c.isalnum())


        l, r = 0, len(alphanum) - 1

        while l < r:
            if alphanum[l] != alphanum[r]:
                return False
            l += 1
            r -= 1
        

        return True

        



        