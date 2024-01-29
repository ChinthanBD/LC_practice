# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # temp = head
        # count = 0
        # while temp:
        #     count +=1
        #     temp = temp.next
        # if count == n:
        #     return head.next

        # temp = head

        # for i in range(count - n -1):
        #     temp = temp.next
        
        # temp.next = temp.next.next
        # return head
        
        fp =head
        sp = head
        for i in range(n):
            fp = fp.next
        if not fp:
            return head.next
        while fp.next:
            sp = sp.next
            fp = fp.next
        sp.next = sp.next.next

        return head

