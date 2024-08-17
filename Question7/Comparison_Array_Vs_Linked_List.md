Comparison of Array vs. Linked List:
Array (Python List):
    • Advantages of using array:
1. Array provides random access to the element. Arrya are indexed. Hence, we can use index of list to directly access the element in constant time, O(1).

2. It has a very simple implementation.

3. Arrays are more memory efficienct in comparison to linked list as they don’t require extra space for pointers.

    • Disadvantages of using array:
1.  In an array, the data are stored in a contiguous way.  To insert an element between the array, t we have to push other elements to create a space at that particular location, which is very time-consuming.
      
2. Array stores element in continus block of memory. Hence it has a fixed size meaning when additional elements are added, the entire array might get shifted to another memory space.  
Linked List:
      
    • Advantages of using Linked List:
1. Linked lists stores data in random moemory location. It is not sequential like array. Hence their size can grow or shrink dynamically during runtime.

2. Insetion and deletion of data at any node is very easy and time saving. Nodes can be inserted and deleted dynamically.


    • Disadvantages of using Linked List:

1. Unlike array, Linked lists are not indexed. Hence they do not provide random access to elements. To access an element in a linked list, we have to start at the beginning of the list and traverse through the list until we find the element.  It takes time complexity O(n).

2. Each node in a linked list requires an extra memory space to store a pointer/reference to the next element. So, we need more space to store even an element in Linked list than in comparison to the array.

3. Implementation of linked list is very complex and not recommended for small sized data.
