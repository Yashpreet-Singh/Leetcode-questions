# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        nodes=[]
        nodes1=[]

        def compare(root):
            
            if root is None:
                return nodes

            if root.left is None and root.right is None:
                nodes.append(root.val)
               
        
            l=compare(root.left)
            r=compare(root.right)

        

        # self.leafSimilar(root2.left)
        # self.leafSimilar(root2.right)

        

        compare(root1)
        nodes1=nodes
        nodes=[]
        compare(root2)

    
        return nodes1==nodes


----------------------------------------------------------

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaf_values(root, leaf_values):
            if not root:
                return
            if not root.left and not root.right:
                leaf_values.append(root.val)
            collect_leaf_values(root.left, leaf_values)
            collect_leaf_values(root.right, leaf_values)

        leaf_values1 = []
        leaf_values2 = []

        collect_leaf_values(root1, leaf_values1)
        collect_leaf_values(root2, leaf_values2)

        return leaf_values1 == leaf_values2
