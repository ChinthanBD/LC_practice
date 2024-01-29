# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def findKth(self, node, k):
        count = 0
        while node:
            count +=1
            if count == k:
                return node
            node = node.next
        return None


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            tail = self.findKth(head, k)
            if not tail:
                break
            next_head = tail.next
            tail.next = None  # Cut off the sublist
            prev.next = self.reverseList(head)  # Reverse the sublist
            head.next = next_head  # Connect the reversed sublist with the next sublist
            prev = head  # Update prev to the last node of the reversed sublist
            head = next_head  # Move head to the beginning of the next sublist
        return dummy.next