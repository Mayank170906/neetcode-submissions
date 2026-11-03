# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        if head.next==None:
            return head
        temp=head
        child=temp.next
        while child.next !=None:
            t=child.next
            child.next=temp
            temp=child
            child=t
        child.next=temp
        head.next=None
        return child