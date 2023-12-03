class Listnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = None
    def __str__(self):
        return f"Listnode(value={self.val})"
for i in [8,0,7]:
    l = Listnode(i)
    l.next = l

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x=""
        y=""
        num = 0
        node1=l1
        node2=l2
        while(node1!=None or node2!=None):
            x+= str(node1.val) if node1 else str(0)
            y+= str(node2.val) if node2 else str(0)
            node1 = node1.next if node1 else None
            node2= node2.next if node2 else None
        num = str(int(x[::-1]) + int(y[::-1]))
        temp = ListNode()
        l = temp
        for i in num[::-1]:
            l.next = ListNode(i)
            l = l.next     
        return temp.next  