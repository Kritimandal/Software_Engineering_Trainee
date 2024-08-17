#Question 8: Python valid_square() Function
import math #importing math module

def valid_square(value): #define valid_square function
    sq_root = math.sqrt(value) #calculate square root
    if sq_root.is_integer():  #check if square root is interger  
        print(f"The number {value} is valid square number. The square root is {sq_root}" ) #print is valid square
    else:
        print(f"The number {value} is not a valid square number." ) #print not a valid square

input_number = int( input('Enter a number:') ) #taking input from the user
valid_square(input_number) #function callback