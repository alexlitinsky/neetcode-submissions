class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        parMap = { ")" : "(", "]" : "[", "}" : "{" }

        for p in s:
            if p == "(" or p == "{" or p =="[":
                st.append(p)
            else:
                if not st or parMap[p] != st[-1]:
                    return False
                st.pop()

        


        return not st