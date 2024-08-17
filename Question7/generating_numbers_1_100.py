
#Question 7. Generating Numbers from 1 to 100

#using array

number_list = list(range(1, 101))  #generating a list of numbers from 1- 100

print("Generating numbers from 1 to 100 using array",number_list)  #print generated list

#using linked list

class LinkedListNode:  # Define LinkedListNode class
    def __init__(self, value, next_node=None):  # Constructor to initialize the node object
        self.value = value  # Set the node's value
        self.next_node = next_node  # Set the reference to the next node

class LinkedList:  # Define LinkedList class
    def __init__(self, head=None):  # Constructor to initialize the LinkedList object
        self.head = head  # Initialize the head of the linked list
        
    def insert(self, value):  # Method to insert a new node with the given value
        new_node = LinkedListNode(value)  # Create a new node
        if self.head is None:  # If the linked list is empty, set the new node as the head
            self.head = new_node
        else:
            current_node = self.head  # Start from the head of the list
            while current_node.next_node:  # Traverse to the last node
                current_node = current_node.next_node
            current_node.next_node = new_node  # Append the new node at the end of the list
        
    def printLinkedList(self):  # Method to print the linked list
        head_node = self.head  # Start from the head node
        print("\nGenerating numbers from 1 to 100 using linked list:", end=" ")
        while head_node:  # Traverse through the linked list
            print(head_node.value, end=" -> ")  # Print the value of each node
            head_node = head_node.next_node  # Move to the next node
        print("Null\n")  # Indicate the end of the linked list

# Create a linked list instance
linked_list = LinkedList()

# Insert numbers 1 to 100 into the linked list
for i in range(1, 101):
    linked_list.insert(i)

# Print the linked list
linked_list.printLinkedList()

		

