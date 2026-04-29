class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        charType = {"(": ")",
                    "[": "]",
                    "{": "}"
                    }

        for char in s: 
            if char not in charType:
                stack.append(char)
            else: 
                if not stack or stack[-1] != charType[char]:
                    return False
                stack.pop()

        return not stack

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        charType = {"(": ")",
                    "[": "]",
                    "{": "}"
                    }

        for char in s: 
            if char in charType:
                stack.append(char)
            else: 
                if not stack or charType[stack[-1]] != char:
                    return False
                stack.pop()

        return not stack


  