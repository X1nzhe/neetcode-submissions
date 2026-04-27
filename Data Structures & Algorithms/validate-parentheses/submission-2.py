class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in s:
            if i in bracket_map:
                stack.append(i)
            else:
                if not stack or i != bracket_map[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0

        