class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with no nodes

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            tail = self.head
            while tail.next:  # Traverse to the last node
                tail = tail.next
            tail.next = new_node  # Point the last node's next to new node
            new_node.prev = tail  # Point the new node's previous to the last node

    def traverse_forward(self):
        node = self.head
        while node:
            print(node.data, end=" <-> ")
            node = node.next
        print("None")

    def traverse_backward(self):
        node = self.head
        while node and node.next:  # Move to the last node
            node = node.next
        while node:
            print(node.data, end=" <-> ")
            node = node.prev
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

dll.traverse_forward()   # Output: 1 <-> 2 <-> 3 <-> None
dll.traverse_backward()  # Output: 3 <-> 2 <-> 1 <-> None
