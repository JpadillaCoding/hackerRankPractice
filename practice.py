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

# Example usage
values = [4, 2, 7, 1, 3, 6, 9]
root = build_tree(values)

def invertTree(root):
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp

        invertTree(root.left)
        invertTree(root.right)
    return root
newRoot = invertTree(root)
def printRoot(root):
    
    if root:
        print(root.left.value)
        print(root.right.value)

        printRoot(root.left)
        printRoot(root.right)

printRoot(newRoot)