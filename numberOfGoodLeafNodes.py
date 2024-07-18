
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/submissions/1325455370/?envType=daily-question&envId=2024-07-18
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return []
            
            if not node.right and not node.left:
                return [1]
            
            left =  dfs(node.left)
            right = dfs(node.right)


            for d1 in left:
                for d2 in right:
                    if d1 + d2 <= distance:
                        self.ans+=1
            all_distance = left + right
            return [d+1 for d in all_distance]
        
        dfs(root)

        return self.ans
            
