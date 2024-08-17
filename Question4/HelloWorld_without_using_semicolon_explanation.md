Question 4: Printing “Hello World” in Java without using semicolon.

Ans: I have used a if method to print the Hello World without using semicolon.  In Java, semicolon is used as a termination of statement.  It tells the compiler where to end the instruction for specific statement. Java statement must end with semicolon. However, if statement has {..} which do not require semicolon. This is because curly braces has termination characteristics. So, we can use if statement for printing “Hello World”. 

If statement checks the condition written inside parenthesis. 
i.e System.out.printf("Hello World") == null 

The condition is always false because printf returns  non null PrintStream. However, the code within the if parenthesis is executed before the condition is checked.  Hence, we get Hello World as output.  
