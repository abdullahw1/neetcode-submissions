# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        # PHASE 1: Find the middle (Slow/Fast Pointers)
        slow = head
        fast = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        # PHASE 2: Split and Reverse the second half
        # 'slow' is at the middle. Let's reverse everything after it.
        prev = None
        curr = slow.next
        slow.next = None # <--- Important! Cut the list in two.
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # 'prev' is now the head of the reversed second half
            
        # PHASE 3: The Zipper Merge
        first = head 
        second = prev
        while second: # Second list is always equal or shorter
            # Step 1: Save lifeboats
            tmp1 =first.next 
            tmp2 = second.next
            
            # Step 2: Re-wire
            first.next = second
            second.next = tmp1
            
            # Step 3: Move pointers forward
            first = tmp1 
            second = tmp2