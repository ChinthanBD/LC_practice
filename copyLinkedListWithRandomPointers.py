# https://leetcode.com/problems/copy-list-with-random-pointer/description/



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mpp = {}
        temp = head
        while temp:
            newNode = Node(temp.val)
            mpp[temp]= newNode
            temp = temp.next
        
        temp = head
        while temp:
            mpp[temp].next = mpp.get(temp.next)
            mpp[temp].random =  mpp.get(temp.random)
            temp = temp.next
        return mpp[head]
        ####################################
