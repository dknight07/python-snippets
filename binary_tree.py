class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def pre_order_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    def in_order_traversal(self, start, traversal):
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    def post_order_traversal(self, start, traversal):
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "PreOrder":
            return "PreOrder Traversal: " + self.pre_order_traversal(tree.root, "")
        elif traversal_type == "InOrder":
            return "InOrder Traversal: " + self.in_order_traversal(tree.root, "")
        elif traversal_type == "PostOrder":
            return "PostOrder Traversal: " + self.post_order_traversal(tree.root, "")
        else:
            print("Traversal Type not found.")


#   BINARY TREE
#      1
#    /  \
#   2       3
#  / \     / \
# 4    5  8    9
#     / \     / \
#    6   7  10  11

# Pre- Order = Root-> Left -> Right = 1,2,4,5,6,7,3,8,9,10,11
# In-Order = Left -> Root -> Right = 4,2,6,5,7,1,8,3,10,9,11
# Post -Order = Left -> Right -> Root = 4,6,7,5,2,8,10,11,9,3,1
# ways to traverse in Depth First Search : InOrder , PreOrder, PostOrder


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(6)
tree.root.left.right.right = Node(7)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)
tree.root.right.right.left = Node(10)
tree.root.right.right.right = Node(11)

print(tree.print_tree("PreOrder"))
print(tree.print_tree("InOrder"))
print(tree.print_tree("PostOrder"))
