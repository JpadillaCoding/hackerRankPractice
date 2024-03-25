class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs to go in per row
        # if both have not null then add together 
        # if only one had a node then the pointer should be the rest 
        if root1 is None and root2 is None:
            return None
        elif root1 is None and root2:
            return root2
        elif root1 and root2 is None:
            return root1
        def recursiveMerge(root1, root2):
            curr = TreeNode(root1.val + root2.val)
            if root1.left is None and root2.left:
                curr.left = root2.left
            elif root1.left and root2.left is None:
                curr.left = root1.left
            else:
                curr.left = recursiveMerge(root1.left, root2.left)
            if root1.right is None and root2.right:
                curr.right = root2.right
            elif root1.right and root2.right is None:
                curr.right = root1.right
            else:
                curr.right = recursiveMerge(root2.right, root2.right)

            return curr
        return recursiveMerge(root1, root2)