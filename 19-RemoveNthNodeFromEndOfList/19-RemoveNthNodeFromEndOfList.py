# Last updated: 6/3/2026, 9:17:45 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n>0:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next