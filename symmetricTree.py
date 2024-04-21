# https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Base case: if both nodes are None, they are symmetric
            if not left and not right:
                return True
            # If one of the nodes is None or their values are different, they are not symmetric
            if not left or not right or left.val != right.val:
                return False
            # Recursively check if the left subtree of the left node is symmetric to the right subtree of the right node,
            # and if the right subtree of the left node is symmetric to the left subtree of the right node
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        # If the root is None, it is symmetric
        if not root:
            return True
        # Check if the left and right subtrees of the root are symmetric
        return isMirror(root.left, root.right)
