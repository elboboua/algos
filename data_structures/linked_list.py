class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def contains(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False
    
    def delete(self, value):
        temp = self.head
        # check is head is the node to be deleted
        if temp and temp.value == value:
            self.head = temp.next
            temp = None
            return
        
        # search for value
        while temp.next is not None:
            if temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next
        return
    
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, " ")
            temp = temp.next
        print("")


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.delete(2)
ll.insert(40)
ll.delete(40)
print(ll.contains(1))
print(ll.contains(50))
ll.print()