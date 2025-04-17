// MY SOLUTION 

/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    // Functions go sequentially, might have to use a for loop

    // How to decompose what is in the function itself? 

    return function(x) {
       if (functions.length == 0) {
        return x; // NOT SURE 
       } else { 
        for (let i = functions.length - 1; i >= 0; i--) {
            f = functions[i]; // Assuming this is a function 
            x = f(x); 
        }
        return x;
       }
    }
};

// BASE CASE 
let fn = compose([x => x + 1, x => 2 * x]);
console.log(fn(4)); // 9

// Example 1
fn = compose([x => x + 1, x => x * x, x => 2 * x]);
console.log(fn(4)); // 65

// Example 2 
fn = compose([x => 10 * x, x => 10 * x, x => 10 * x]);
console.log(fn(1)); // 1000

// Example 3 
fn = compose([]);
console.log(fn(42)); // 42

// ** BEST SOLUTION ** 

var compose = function(functions) {
    return function(x) {
        for (let i = functions.length - 1; i >= 0; i--) {
            x = functions[i](x);
        }
        return x; 
    };
};

/* 

- Combine both function retreival and call in one line to reduce complexity! 
- If length = 0; it will not iterate through the for loop! 

*/