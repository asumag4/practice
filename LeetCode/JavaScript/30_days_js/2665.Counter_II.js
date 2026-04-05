// MY SOLUTION 

var createCounter = function(init) {
    let counter = init;
    return {
        increment: () => {
            return ++counter;
        },
        decrement: () => {
            return --counter;
        },
        reset: () => {
            counter = init;
            return counter;
        },
    }
};

/* 

NOTE: The major difference is in using pre-increment and 
post-increment, the difference is that WHEN the value is returned!
If you want the operation to occur immediately after with the correct
value; then you should use pre-increment! (It's not like Python)

*/

// ** BEST SOLUTION ** 

var createCounter = function(init) {
    const savedInt = init;
    let increment = () => {
        return ++init
    };
    let decrement = () => {
        return --init
    };
    let reset = () => {
        init = savedInt
        return init;
    }
    return {increment , decrement , reset}
};
const counter = createCounter(5);
counter.increment();