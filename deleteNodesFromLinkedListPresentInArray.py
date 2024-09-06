# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/submissions/1381119769/?envType=daily-question&envId=2024-09-06
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        lookup_set = set(nums)

        dummy = ListNode(0, head)
        current = dummy

        while current.next:
            if current.next.val in lookup_set:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next
