class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        container = []
        for i in tokens:
            if( i == "+"):
                a = container.pop() + container.pop()
                container.append(a)
            elif(i == "-"):
                a = container.pop()
                b= container.pop()
                container.append((b-a))
            elif(i == "*"):
                a = container.pop() * container.pop()
                container.append(a)
            elif(i == "/"):
                a = container.pop()
                b = container.pop()
                container.append(int(b/a))
            else:
                container.append(int(i))
        return container.pop()                    
