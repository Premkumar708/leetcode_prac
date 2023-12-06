class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        blocks = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        for i in s:
            if i in blocks:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if i != blocks[stack.pop()]:
                        return False
        return len(stack) == 0    