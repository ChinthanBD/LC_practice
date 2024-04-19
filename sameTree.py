# https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverseTrees(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return traverseTrees(a.left, b.left) and traverseTrees(a.right, b.right)

        # Return the result of the recursive comparison
        return traverseTrees(p, q)