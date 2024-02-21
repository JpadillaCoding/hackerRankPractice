class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root

def build_tree(values):
    root = None
    for value in values:
        root = insert(root, value)
    return root

def invertTree(root):
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp

        invertTree(root.left)
        invertTree(root.right)
    return root
def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.value)
        inorder_traversal(root.right, result)

# Original tree
original_values = [4, 2, 7, 1, 3, 6, 9]
original_root = build_tree(original_values)

# Invert the tree
inverted_root = invertTree(original_root)

# Perform in-order traversal on both original and inverted trees
original_result = []
inverted_result = []

inorder_traversal(original_root, original_result)
inorder_traversal(inverted_root, inverted_result)

print(inverted_result)