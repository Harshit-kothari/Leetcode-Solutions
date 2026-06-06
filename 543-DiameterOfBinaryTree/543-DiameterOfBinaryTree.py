# Last updated: 6/6/2026, 7:32:27 PM
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Just call the external helper
        return compute_diameter(root)


# 🔹 Function outside the class
def compute_diameter(root: Optional[TreeNode]) -> int:
    max_diameter = [0]   # use list to mutate inside dfs
    
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        # update diameter at this node
        max_diameter[0] = max(max_diameter[0], left_height + right_height)
        
        # return height of this subtree
        return 1 + max(left_height, right_height)
    
    dfs(root)
    return max_diameter[0]