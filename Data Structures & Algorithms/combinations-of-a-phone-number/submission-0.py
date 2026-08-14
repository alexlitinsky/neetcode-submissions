class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        res = []
        curr = []
        comboDict = {"2" : list("abc"),
                     "3" : list("def"),
                     "4" : list("ghi"),
                     "5" : list("jkl"),
                     "6" : list("mno"),
                     "7" : list("pqrs"),
                     "8" : list("tuv"),
                     "9" : list("wxyz")}
        
        def backtrack(i):
            if i == len(digits):
                res.append("".join(curr[:]))
                return
          
            for l in comboDict[digits[i]]:
                curr.append(l)
                backtrack(i + 1)
                curr.pop()
        

        backtrack(0)

        return res
        