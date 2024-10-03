# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#remember 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        node1=[]
        node2=[]
        def check(root,node):

            if root is None:
                return root

            if root.left is None and root.right is None:
                return root.val #returns the value to main if just one root value is there

            l=check(root.left,node)
            r=check(root.right,node)

            node.extend([l,r,root.val])

        l=check(p,node1) 
       
        if l is not None:
            node1.append(l)

        r=check(q,node2)
      
        if r is not None:
            node2.append(r)
        
        
        return node1==node2



----------------------------------------------------------------

def isSameTree(p, q): 
if not p and not q:
  return True 
if not por not q: 
  return False
if p.val != q.val: 
  return False 

return (isSameTree(p.left, q.left) isSameTree(p.right, q.right))




        
