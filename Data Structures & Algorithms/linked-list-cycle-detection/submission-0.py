# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head ==None or head.next ==None:
            return False
        x=head
        y=head.next
        while y!=None and y.next!=None:
            if x==y:
                return True
            x=x.next
            y=y.next.next
        return False