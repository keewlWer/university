class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right) 
    traverse(root)
    return result

# Приклади:

# Приклад 1:
# Дерево: [1,null,2,3]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.right = TreeNode(3)
print(inorderTraversal(root1))  # Output: [1, 2, 3]

# Приклад 2:
# Дерево порожнє
root2 = None
print(inorderTraversal(root2))  # Output: []

# Приклад 3:
# Дерево: [1]
root3 = TreeNode(1)
print(inorderTraversal(root3))  # Output: [1]
