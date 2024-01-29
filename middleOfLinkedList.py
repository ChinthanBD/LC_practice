# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = head
        fp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        return sp