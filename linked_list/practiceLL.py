class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeigin(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    def traverse(self):
        
        curr = self.head
        
        while curr:
            print(curr.data, end="->")
            curr = curr.next
            
    def remove_duplicate(self):
        current = self.head
        
        while current and current.next:
            
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
                

linked_list = LinkedList()

linked_list.insertAtBeigin(1)
linked_list.insertAtBeigin(1)
linked_list.insertAtBeigin(2)
linked_list.insertAtBeigin(3)
linked_list.append(4)
linked_list.remove_duplicate()
linked_list.traverse()