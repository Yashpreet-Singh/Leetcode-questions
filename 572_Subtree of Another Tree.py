# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q): 
            if not p and not q:
                return True 
            if not p or not q: 
                return False
            if p.val != q.val: 
             return False 

            return (isSameTree(p.left, q.left)) and (isSameTree(p.right, q.right))



        if root == None:
            return False
        
        if isSameTree(root,subRoot):
            return True

        return (self.isSubtree(root.left,subRoot)) or (self.isSubtree(root.right,subRoot))

#-----------------------------------------Preorder traversal for graphs---------------- time: O(m*n)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s:
            return True
        return False
    
    
    def traverse_tree(self, s):
        if s:
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None


'''
You use it as a delimiter between the nodes in the string representation.

This is because: take a test case of [12], [2]. So we have our root with val=12 and no children, and subRoot node with val=2 and no children. If we turn them to string without the #, we get the following root="12 None None" and subRoot ="2 None None". This results in a false positive since the string "2 None None" is a substring of "12 None None". If we add a # to the beginning of every node with a value, we get root="#12 None None" and subRoot="#2 None None". Now, subRoot's string is no longer a substring of root's string and doesn't create a false positive anymore.

In fact, we can replace the # character with basically any letter (e.g. h) since all it needs to do is delimit (but we can't use a number as a delimiter!)
'''
