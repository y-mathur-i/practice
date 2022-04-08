from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        fast = head
        while n != 0:
            fast = fast.next
            n -= 1
        if fast is None:
            return head.next
        while fast.next:
            curr = curr.next
            fast = fast.next
        # print(curr.next.val)
        curr.next = curr.next.next 
        return head
