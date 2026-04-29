
class Solution:
    def isValid(self, s: str) -> bool:
        charType = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char not in charType:
                stack.append(char)
            else:
                if not stack or stack[-1] != charType[char]:
                    return False
                stack.pop()

        return not stack
