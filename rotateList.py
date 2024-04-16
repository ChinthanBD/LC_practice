# https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the list and locate the last node
        length = 1
        last_node = head
        while last_node.next:
            length += 1
            last_node = last_node.next

        # Adjust k to get the effective rotation amount
        k = k % length
        if k == 0:
            return head  # No rotation needed

        # Move the last node to the beginning to perform rotation
        last_node.next = head  # Make the list circular
        new_last_node = head
        for _ in range(length - k - 1):
            new_last_node = new_last_node.next
        new_head = new_last_node.next
        new_last_node.next = None  # Break the circular list

        return new_head

