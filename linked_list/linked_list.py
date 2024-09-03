class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)

        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Otherwise, traverse to the end of the list and append the new node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        # Start from the head and traverse the list, printing each node's data
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def _find_middle(self, head):
        # This function uses the "slow and fast pointer" technique to find the middle node
        if head is None:
            return head

        slow = head  # Slow pointer moves one step at a time
        fast = head  # Fast pointer moves two steps at a time

        # When the fast pointer reaches the end, the slow pointer will be at the middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _sorted_merge(self, left, right):
        # Base cases: If one list is empty, return the other
        if left is None:
            return right
        if right is None:
            return left

        # Compare the data in the two nodes and recursively merge the rest of the list
        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)

        return result

    def _merge_sort(self, head):
        # Base case: If the list is empty or has only one element, it's already sorted
        if head is None or head.next is None:
            return head

        # Step 1: Find the middle of the list
        middle = self._find_middle(head)
        next_to_middle = middle.next

        # Step 2: Split the list into two halves
        middle.next = None

        # Step 3: Recursively sort each half
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        # Step 4: Merge the two sorted halves
        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def sort(self):
        # This function initiates the merge sort on the linked list
        self.head = self._merge_sort(self.head)
    
    def reverse(self):
        

# Example usage
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("Original Linked List:")
llist.print_list()

llist.sort()

print("Sorted Linked List:")
llist.print_list()
