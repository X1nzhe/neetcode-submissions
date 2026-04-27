class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            
            if token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                y = stack.pop()
                x = stack.pop()
                stack.append(x-y)
            elif token == "*":
                y = stack.pop()
                x = stack.pop()
                stack.append(x*y)
            elif token == '/':
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(token))
        return stack[-1]

        