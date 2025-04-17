/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    // Append all the arguments together 

    // How do you handle all the args together? 
    return args.length;

};

// BASE CASE 
console.log(argumentsLength(1, 2, 3)); // 3

// Test case 1 
console.log(argumentsLength(5)) // 1

// Test case 2
console.log(argumentsLength({}, null, "3")) // 3 

// ** BEST SOLUTION **

var argumentsLength = (...args) => args.length;
