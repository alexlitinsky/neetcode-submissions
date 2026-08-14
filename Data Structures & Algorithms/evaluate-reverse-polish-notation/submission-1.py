class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:
            if t in "+-*/":
                right = int(stack.pop())
                left = int(stack.pop())
                if t == "+": stack.append(left + right)
                elif t == "-": stack.append(left - right)
                elif t == "*": stack.append(left * right)
                elif t == "/": stack.append(left / right)
            else:
                stack.append(t)
        
        return int(stack[-1])



            
        