# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root: Optional[TreeNode])->int:
            if(not root):
                return 0
            L = depth(root.left)
            if L == -1: return -1 

            R = depth(root.right)
            if R == -1: return -1

            if abs(L - R) > 1:
                return -1
            return 1+max(L, R)
        return depth(root)!=-1

        