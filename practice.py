class Solution:
    def inorderTraversal(self, root):
        result = []

        def traverse(root, result):
            if root is None:
                return None
            traverse(root.left, result)
            result.append(root.val)
            traverse(root.right, result)
        traverse(root, result)
        return result