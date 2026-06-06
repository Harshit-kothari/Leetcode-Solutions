# Last updated: 6/6/2026, 7:32:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if not root:
        return 0
    return (1+max(height(root.left),height(root.right)))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return height(root)        