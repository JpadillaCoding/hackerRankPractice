def maxDepth(self, root: Optional[TreeNode], counter = 1) -> int:
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))