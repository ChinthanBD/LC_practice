# https://leetcode.com/problems/split-linked-list-in-parts/submissions/1383499010/?envType=daily-question&envId=2024-09-08
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        curr = head
        length = 0

        while curr:
            curr = curr.next
            length +=1
        

        base_length, remainder = length // k, length % k

        curr = head
        res = []
        for _ in range(k):
            res.append(curr)

            for _ in range(base_length - 1 + (1 if remainder else 0)):
                if not curr: break
                curr = curr.next

            remainder -=(1 if remainder else 0)
            if curr:
                curr.next, curr = None, curr.next
        
        return res

