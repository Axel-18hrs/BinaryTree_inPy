from BinaryTree import BinaryTree
#
tree = BinaryTree()

tree.insert(5)
tree.insert(8)
tree.insert(2)
tree.insert(10)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.insert(2)

print(tree.search(4))
print(tree.search(3))

print(tree.delete(4))
print(tree.delete(8))

print(tree.search(5))
print(tree.search(8))
