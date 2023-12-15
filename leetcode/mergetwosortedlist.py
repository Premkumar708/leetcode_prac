# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x=[]
        y=[]
        while list1 is not None:
            x.append(list1.val)
            list1=list1.next
        while list2 is not None:
            y.append(list2.val)
            list2= list2.next
        z = sorted(x+y)
        l = ListNode()
        temp = l
        for i in z:
            temp.next= ListNode(i)
            temp=temp.next
        return l.next  