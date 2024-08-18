//Reversing a string using JavaScript


let input_string = prompt("Please, enter a string?"); // Prompts for string user input

function reverseString(str) {  //Defining function which takes string as input 

    return str.split("").reverse().join(""); //splitting individual character of string to array, reversing it the joining it back to string
    
} //end  reverseString function
reversedString = reverseString(input_string); //function call with input string
console.log(reversedString); //print output
