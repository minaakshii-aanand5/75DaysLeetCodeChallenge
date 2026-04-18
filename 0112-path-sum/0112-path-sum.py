class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # recursive check
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
        