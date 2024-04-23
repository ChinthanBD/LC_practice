# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Optional
# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        # Calculate the size of the left subtree
        left_subtree_size = mid
        
        # Recursive call to construct the left subtree
        root.left = self.buildTree(preorder[1:1+left_subtree_size], inorder[:mid])
        
        # Recursive call to construct the right subtree
        root.right = self.buildTree(preorder[1+left_subtree_size:], inorder[mid+1:])
        
        return root