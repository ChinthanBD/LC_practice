# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        while temp.next:
            val1 = temp.val
            val2 = temp.next.val
            gcd_val = self.gcd(val1, val2)
            Node = ListNode(gcd_val)
            next_node = temp.next
            temp.next = Node
            Node.next = next_node
            temp = next_node
        return head

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
