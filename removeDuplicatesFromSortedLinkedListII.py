# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                # Skip over all duplicates
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Skip the last duplicate
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
                
        return dummy.next
