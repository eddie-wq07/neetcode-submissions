class Solution:
    def isValid(self, s: str) -> bool:
        paran = {
            "}" : "{", 
            ")" : "(",
            "]" : "["
        }

        stack = []

        for c in s: 
            if c == "{" or c == "(" or c == "[": 
                stack.append(c)
            elif stack and stack[-1] == paran[c]:
                stack.pop()
            else: 
                return False

        return not stack

        