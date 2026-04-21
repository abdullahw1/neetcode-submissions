# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None
        if p is None and q is None:
            return True
        
        # One is None, the other isn't
        if p is None or q is None:
            return False
        
        # Both nodes exist, check if values are equal and recursively check subtrees
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)