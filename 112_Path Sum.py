# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        if root is None:
            return False # for base condition
            
        targetSum = targetSum - root.val 
        #leafnode
        if root.left is None and root.right is None:
            if targetSum==0:
                return True
            else:
                return False
  

        l=self.hasPathSum(root.left, targetSum)
        r=self.hasPathSum(root.right, targetSum)


        return l or r
        
