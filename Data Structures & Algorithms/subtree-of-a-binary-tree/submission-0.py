# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _sameTree(self, tree1, tree2) -> bool:
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        return self._sameTree(tree1.left, tree2.left) and self._sameTree(tree1.right, tree2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        if self._sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        