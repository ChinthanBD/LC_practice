# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # hashlist = []
        # while headA:
        #     hashlist.append(headA)
        #     headA = headA.next
        # while headB:
        #     if headB in hashlist:
        #         return headB
        #     headB = headB.next
        # return None
        ####################################
        # c1 = 0
        # c2 = 0
        # temp1 = headA
        # temp2 = headB
        # while headA:
        #     c1 += 1
        #     headA = headA.next
        # while headB:
        #     c2 += 1
        #     headB = headB.next
        
        # if c1> c2:
        #     for i in range(c1-c2):
        #         temp1 = temp1.next
        # else:
        #     for i in range(c2-c1):
        #         temp2 = temp2.next
        
        # while temp1 and temp2:
        #     if temp1 == temp2:
        #         return temp1
        #     temp1 = temp1.next
        #     temp2 = temp2.next
        # return None
        ###################################

        temp1 = headA
        temp2 = headB
        if not temp1 or not temp2:
            return None
        
        while(temp1 != temp2):
            temp1 = temp1.next
            temp2 = temp2.next
            if temp1 == temp2:
                return temp1
            if not temp1:
                temp1 = headB
            if not temp2:
                temp2 = headA
        
        return temp1

