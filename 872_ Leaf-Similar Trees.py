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



        
