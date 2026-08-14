class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur = []
        def backtrack(openP, closeP):
            if openP == n and closeP == n:
                res.append("".join(cur[:]))
                return
            
            if openP < n:
                cur.append("(")
                backtrack(openP + 1, closeP)
                cur.pop()
            if closeP < openP:
                cur.append(")")
                backtrack(openP, closeP + 1)
                cur.pop()

            
        backtrack(0, 0)

        return res
        