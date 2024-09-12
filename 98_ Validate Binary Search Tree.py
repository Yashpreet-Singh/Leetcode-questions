# Definition for a binary tree node.
#https://www.hellointerview.com/learn/code/depth-first-search/validate-binary-search-tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkbst(root,min_,max_):
            
            #An empty tree is a valid binary search tree.
            if root is None:
                return True
            
            # check if the current node's value is within the valid range
            if root.val >= max_ or root.val <= min_:
                return False
            
            
            l=checkbst(root.left,min_,root.val)
            r=checkbst(root.right,root.val,max_)

            return l and r
        
        return checkbst(root,float('-inf'), float('inf'))
