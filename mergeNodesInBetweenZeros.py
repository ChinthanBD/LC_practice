
# https://leetcode.com/problems/merge-nodes-in-between-zeros/submissions/1310364058/?envType=daily-question&envId=2024-07-04
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to act as the new head
        current = dummy  # Pointer to build the new list
        val = 0  # Accumulator for values
        head = head.next  # Skip the initial zero node
        
        while head:  # Traverse the list
            if head.val == 0:  # When a zero node is encountered
                newNode = ListNode(val)  # Create a new node with the accumulated value
                current.next = newNode  # Link it to the new list
                current = newNode  # Move the pointer to the new node
                val = 0  # Reset the accumulator
            else:
                val += head.val  # Accumulate the values
            head = head.next  # Move to the next node
        
        return dummy.next  # Return the new list, skipping the dummy node
