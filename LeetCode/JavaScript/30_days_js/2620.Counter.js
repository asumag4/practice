// Solution example by Cosmic_Phantom

// Simple example of closure: 

const makeCounter = () => {
    let count = 0;

    return () => {
        count++;
        console.log(count);
    }
}

let counter = makeCounter(); // Initialize the function, stored as counter var
counter(); // logs 1, counter stores `1`
counter(); // logs 2, the stored val `1` + 1 = 2
counter(); // logs 3, the stored val `2` + 1 = 3

// Applied example of closure:

function add(x) {
    return function(y) {
      return x + y;
    }
  }
  
  let add5 = add(5);
  console.log(add5(3)); // 8

// The whole point is to preserve state! 

// ** SOLUTION **
var createCounter = function(n) {
    return ()=> n++
};

// ** BEST SOLUTION ** 
var createCounter = function(n) {
    let counter = n-1
    return function() {
        counter++
        return counter
    };
};