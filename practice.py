class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            curr = TreeNode(root1.val + root2.val)

            curr.left = self.mergeTrees(root1.left, root2.left)
            curr.right = self.mergeTrees(root1.right, root2.right)
            return curr

        elif root1 and root2 is None:
            return root1
        else:
            return root2