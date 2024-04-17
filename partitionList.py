#https://leetcode.com/problems/partition-list/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create dummy nodes for the two partitions
        less_than = ListNode(0)
        greater_than_equal = ListNode(0)
        
        # Pointers for the two partitions
        less_than_ptr = less_than
        greater_than_equal_ptr = greater_than_equal
        
        # Traverse the original list and partition nodes based on their values
        while head:
            if head.val < x:
                less_than_ptr.next = head
                less_than_ptr = less_than_ptr.next
            else:
                greater_than_equal_ptr.next = head
                greater_than_equal_ptr = greater_than_equal_ptr.next
            head = head.next
        
        # Merge the two partitions
        less_than_ptr.next = greater_than_equal.next
        greater_than_equal_ptr.next = None
        
        # Return the merged list
        return less_than.next
