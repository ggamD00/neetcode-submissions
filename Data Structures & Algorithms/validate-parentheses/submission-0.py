class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0

        while i < len(s):
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    i += 1
                    continue
                else: return False
            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                    i += 1
                    continue
                else: return False
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                    i += 1
                    continue
                else: return False
            stack.append(s[i])
            i += 1
        
        return len(stack) == 0
