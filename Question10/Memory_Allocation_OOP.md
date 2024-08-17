Question 10: Memory Allocation in OOP


In simple word, the memory allocation in the object-oriented programming (OOP) is the process of allocation memory space for an object. It is the process of reserving the memory block in the memory of the computer for storing a data and member function for an object. 

In OOP, the memory spcae for an object is allocated when it’s declared. The member functions are created and placed in memory space only once when they are defined as a part of a class definition. Since all the objects belonging to that class use the same member functions, no separate space is allocated for member functions. When the objects are created only spcae for  member variables in allocated separately for each object. Seperate memory locations for the objects are essentiat because the data will hold different data values for different objects.

 Objects can be allocated memory either on Stack or on Heap depending upon the programming languages. The size of the memory allocated for object depends upon the data size, data type and complexity of it’s member function.   

Memory deallocation is must be done to free up the memory occupied by the object once the object is no longer needed. In some OOP languages, such as Java and C#, memory deallocation is performed automatically by garbage collection. Garbase collection is a process that identifies and removes objects that are not required any longer in program execution.
