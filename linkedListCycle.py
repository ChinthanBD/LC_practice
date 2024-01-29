# https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        sp = head
        fp = head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            if fp == sp:
                return True
        return False
        