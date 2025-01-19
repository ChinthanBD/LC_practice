# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        current, prevLeft = head, dummy
        for _ in range(left-1):
            current =current.next
            prevLeft = prevLeft.next
        
        prev = prevLeft
        for _ in range(right-left+1):
            tmpNext = current.next
            current.next = prev
            prev = current
            current = tmpNext
        
        prevLeft.next.next = current
        prevLeft.next = prev

        return dummy.next
