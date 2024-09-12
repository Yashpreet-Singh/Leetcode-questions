# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        #tilt = []
        tilt=0

        def checktilt(root):
            nonlocal tilt
            if root is None:
                return 0

            if root.left is None and root.right is None:
                return root.val

            left = checktilt(root.left)
            right = checktilt(root.right)

            #tilt.append(abs(left - right))
            tilt+=abs(left - right)
           
            return left + right + root.val

        checktilt(root)
        #return sum(tilt)
        return tilt
