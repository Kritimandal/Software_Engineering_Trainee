//Reversing a string using JavaScript

// Prompts for string input
let input_string = prompt("Please, enter a string?");

//Defining function which takes string as input parameter
function reverseString(str) {  

//splitting individual character of string to array, reversing it the joining it back to string

    return str.split("").reverse().join(""); 
} //end  reverseString function
reversedString = reverseString(input_string); //function call with input string
console.log(reversedString); //print output
