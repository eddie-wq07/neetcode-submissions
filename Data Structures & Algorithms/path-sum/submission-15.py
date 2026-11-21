# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:   
        p = []

        def dfs(root, targetSum):
            if not root:
                return False

            p.append(root.val)

            if not root.left and not root.right: 
                if sum(p) == targetSum:
                    return True
                p.pop()
                return False

            if dfs(root.left, targetSum): 
                return True
            
            if dfs(root.right, targetSum):
                return True

            p.pop()
            return False
        
        return dfs(root, targetSum)





