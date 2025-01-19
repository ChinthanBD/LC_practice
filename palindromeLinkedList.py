# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        helper = []

        tmp = head

        while tmp:
            helper.append(tmp.val)
            tmp =tmp.next
        
        return helper == helper[::-1]

