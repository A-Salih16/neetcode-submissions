# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     
     
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.a=0
        def depth(root: Optional[TreeNode])->int:

            if(not root):
                return 0
            L=depth(root.left)
            R=depth(root.right)
            self.a=max(self.a,L+R) 
            return 1 + max(L, R)
        depth(root)
        return self.a


        