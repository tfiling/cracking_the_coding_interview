# https://neetcode.io/problems/valid-binary-search-tree
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MIN_NODE_VALUE = -1000
MAX_NODE_VALUE = 1000


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return (self._is_valid_bst(root.left, MIN_NODE_VALUE, root.val) and
                self._is_valid_bst(root.right, root.val, MAX_NODE_VALUE))

    def _is_valid_bst(self, node: Optional[TreeNode], min_value: int, max_value: int) -> bool:
        if not node:
            return True
        if node.val <= min_value or node.val >= max_value:
            return False
        if node.left and node.left.val >= max_value:
            return False
        if node.right and node.right.val <= min_value:
            return False
        return (self._is_valid_bst(node.left, max(MIN_NODE_VALUE, min_value), node.val) and
                self._is_valid_bst(node.right, node.val, min(MAX_NODE_VALUE, max_value)))


if __name__ == '__main__':
    tree = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    sol = Solution()
    print(sol.isValidBST(tree))