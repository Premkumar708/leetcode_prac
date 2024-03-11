class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if( i == '+'):
                a = stack[-1] + stack[-2]
                stack.append(a)
            elif( i == "D" ):
                a = stack[-1]
                stack.append(a*2)
            elif( i == 'C'):
                stack.pop()
            else:
                stack.append(int(i))    
        return sum(stack)                         
