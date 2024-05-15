# https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        sorted_values = inorder_traversal(root)

        min_diff = float('inf')
        for i in range(1, len(sorted_values)):
            min_diff = min(min_diff, abs(sorted_values[i] - sorted_values[i-1]))

        return min_diff
