def minDepth(self, root: Optional[TreeNode]) -> int:
    # implement bfs
    # want the count to stop if it's an edge
    if not root:
        return 0
    q = deque([root])
    counter = 1
    while q:

        for i in range(len(q)):
            node = q.popleft()
            if not node.left and not node.right:
                return counter
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        counter = counter + 1
    return counter 