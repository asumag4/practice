// *** MY SOLUTION **

var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World"
    }
};

// ** BEST SOLUTION **
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
    }
};