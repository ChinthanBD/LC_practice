#https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        # Initialize pointers
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # Move pre pointer to the node just before the sublist to be reversed
        for _ in range(left - 1):
            pre = pre.next

        # Reverse the sublist between left and right
        curr = pre.next
        for _ in range(right - left):
            temp = pre.next
            pre.next = curr.next
            curr.next = curr.next.next
            pre.next.next = temp

        return dummy.next
