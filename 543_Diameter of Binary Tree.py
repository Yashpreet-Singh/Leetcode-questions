'''
-get max depth of current node 
-calculate diameter of each node (left+right), Before returning, I should add those values together to get the diameter of the tree rooted at the current node. 
I can then compare that value to a global variable max_, and update max_ if necessary.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_=0

        def checkdiameter(root):
            nonlocal max_

            if root is None:
                return 0
            


            l=checkdiameter(root.left)
            r=checkdiameter(root.right)

            max_ = max(max_,l+r)

            return max(l,r)+1
        

        
        checkdiameter(root)
        return max_
