class Solution:
    def isValid(self, s: str) -> bool:
        parentMap = { ")" : "(", "}" : "{", "]" : "["}

        stack = []

        for p in s:
            if p not in parentMap:
                stack.append(p)
            elif p in parentMap and stack and parentMap[p] == stack[-1]:
                stack.pop()
            else:
                return False
        

        return True if not stack else False

        