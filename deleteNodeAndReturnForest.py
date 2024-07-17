# https://leetcode.com/problems/delete-nodes-and-return-forest/?envType=daily-question&envId=2024-07-17
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val in to_delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node
        
        if dfs(root):
            forest.append(root)
        
        return forest
