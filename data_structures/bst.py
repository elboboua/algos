# A Binary Search tree
# O(log N) search time
# O(log N) insertion

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.head = None

    def insert(self, value: int) -> None:
        newNode = Node(value) 
        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        while True:
            if value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    break
                else:
                    temp = temp.right

    def search(self, value: int) -> bool:
        if self.head is None:
            return False
        temp = self.head

        while True:
            if value == temp.value:
                return True
            if value < temp.value:
                if temp.left is None:
                    return False
                temp = temp.left
                continue
            if temp.right is None:
                return False
            temp = temp.right

    def delete(self, value: int):
        if self.head is None:
            return
        temp = self.head

        while True:
            if temp.value == value:
                print("found value ", value)
                if temp.left is None and temp.right is None:
                    print("value has no children")
                    temp = None
                    return
                if temp.left is not None and temp.right is None:
                    left = temp.left
                    temp.value = left.value
                    temp.left = left.left
                    temp.right = left.right
                    return
                if temp.left is None and temp.right is not None:
                    right = temp.right
                    temp.value = right.value
                    temp.left = right.left
                    temp.right = right.right
                    return
                # there are two children
                # replace temp with right node and put left node is left most child
                left = temp.left
                right = temp.right
                temp.value = right.value
                temp.left = right.left
                temp.right = right.right
                while temp.left is not None:
                    temp = temp.left
                temp.left = left
                return
            elif temp.value > value:
                if temp.left is None:
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    return
                temp = temp.right

    
    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:  # This condition is added to handle the initial call
                node = self.head
            if node is None:
                return
        self.print_tree(node.right, level + 1)  # Go right first for reverse in-order
        print(' ' * 4 * level + '->', node.value)
        self.print_tree(node.left, level + 1)  # Then go left



bst = BinarySearchTree()
example_list = [5,2,8,3,6,10]
for num in example_list:
    bst.insert(num)

bst.print_tree()

print(f"1 in {example_list}: False: {bst.search(1)}")
print(f"100 in {example_list}: False: {bst.search(100)}")
print(f"-25 in {example_list}: False: {bst.search(-25)}")
print(f"2 in {example_list}: True: {bst.search(2)}")
print(f"6 in {example_list}: True: {bst.search(6)}")

bst.delete(6)
bst.print_tree()
print(f"6 in {example_list}: False: {bst.search(6)}")