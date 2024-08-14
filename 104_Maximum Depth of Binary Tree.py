# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        #leaf node
        if root.left is None and root.right is None:
            return 1
        
        
            
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right) + 1 #+1 for the root node


        '''
      Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once, and at each node, we perform constant time work.
      Space Complexity: O(N), where N is the number of nodes. A total of N call frames have to be allocated, one for each node in the tree.
      '''
