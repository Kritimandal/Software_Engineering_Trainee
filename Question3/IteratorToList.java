import java.util.ArrayList;  // Importing the ArrayList class from java.util package
import java.util.Arrays;     // Importing the Arrays class from java.util package
import java.util.Iterator;   // Importing the Iterator interface from java.util package
import java.util.List;    

public class IteratorToList { //main class
    public static void main(String[] args) { // Entry point of the program
        
       Iterator<Integer> iterator = Arrays.asList(1, 2, 3).iterator(); // generating an iterator

        
        List<Integer> newList = new ArrayList<>();  // defining a list
        while (iterator.hasNext()) { // Convert the iterator to a list
            newList.add(iterator.next());
        }
     
        System.out.println(newList); // Print the list
    } // end main method
} //end main class