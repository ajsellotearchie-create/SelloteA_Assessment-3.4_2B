from collections import deque


# ==========================================
# BINARY TREE IMPLEMENTATION
# ==========================================
class TreeNode:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None


def build_sellote_binary_tree() -> TreeNode:
    """
    Constructs a Complete Binary Tree using the letters of 'SELLOTE':
            S
          /   \
         E     L
        / \   / \
       L   O T   E
    """
    letters = ["S", "E", "L", "L", "O", "T", "E"]
    nodes = [TreeNode(letter) for letter in letters]

    # Link parent and child nodes (level-order)
    nodes[0].left = nodes[1]   # S -> E
    nodes[0].right = nodes[2]  # S -> L
    nodes[1].left = nodes[3]   # E -> L
    nodes[1].right = nodes[4]  # E -> O
    nodes[2].left = nodes[5]   # L -> T
    nodes[2].right = nodes[6]  # L -> E

    return nodes[0]


def tree_bfs(root: TreeNode) -> list[str]:
    """Breadth-First Search (Level-Order Traversal) for Binary Tree."""
    if not root:
        return []

    visited = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        visited.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return visited


def tree_dfs_preorder(root: TreeNode) -> list[str]:
    """Depth-First Search (Pre-Order: Root -> Left -> Right) for Binary Tree."""
    if not root:
        return []

    visited = []
    stack = [root]

    while stack:
        current = stack.pop()
        visited.append(current.value)

        # Push right first so left is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return visited


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("=== ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE (SELLOTE) ===\n")

    root = build_sellote_binary_tree()
    print("====================================================")
    print("BINARY TREE ('S', 'E', 'L', 'L', 'O', 'T', 'E')")
    print("====================================================\n")
    print("   BFS Traversal :", " -> ".join(tree_bfs(root)))
    print("   DFS Traversal :", " -> ".join(tree_dfs_preorder(root)))