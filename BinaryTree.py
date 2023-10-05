from Node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.recursive_insert(self.root, data)

    def recursive_insert(self, node, data):
        # Base case, where we encounter an empty left or right branch
        if node is None:
            print(data)
            return Node(data)

        # To maintain order, we avoid repetitions in node values
        if data == node.data:
            print("this value exists: ", data)
            return node

        # If the new value is smaller than the node's value, we recursively search the left subtree
        # Otherwise, we search the right subtree
        if data < node.data:
            node.left = self.recursive_insert(node.left, data)
        else:
            node.right = self.recursive_insert(node.right, data)

        return node

    def delete(self, data):
        self.root = self.recursive_delete(self.root, data)

    def recursive_delete(self, node, data):
        if node is None:
            return node

        # If the value to delete is smaller, search in the left subtree
        if data < node.data:
            node.left = self.recursive_delete(node.left, data)
        # If the value to delete is larger, search in the right subtree
        elif data > node.data:
            node.right = self.recursive_delete(node.right, data)
        # If we find the value to delete
        else:
            # Case 1: It has no children or only one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 2: It has two children
            # Find the immediate successor in the right subtree
            temp = self.find_min(node.right)
            # Copy the value of the immediate successor to the current node
            node.data = temp.data
            # Delete the immediate successor from the right subtree
            node.right = self.recursive_delete(node.right, temp.data)

        return node

    @staticmethod
    def find_min(node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, data):
        # Search for the node by passing the root node where the graph begins and the value to search for
        found_node = self.recursive_search(self.root, data)
        return found_node.data if found_node else None

    def recursive_search(self, node, data):

        if node is None or node.data == data:
            return node

        if data < node.data:
            return self.recursive_search(node.left, data)
        else:
            return self.recursive_search(node.right, data)
