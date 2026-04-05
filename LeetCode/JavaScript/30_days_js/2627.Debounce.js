/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timer; 
    return function(...args) {
        // Explanation: 
        // 50, [30,60,100] => [80,110,150] => [X,X,O]
        // 35, [30,60,100] => [65, 95, 135] => [X,O,O]

        // Example 1: 
        // 50 [50,75] => [100,125] => [X,O]

        // Example 2: 
        // 20, [50,100] => [70,120] => [O,O]

        // Example 3: 
        // 150, [50, 300, 300]=> [200, 450, 450] => [O, X, O]

        // Calculated the timeouts of each 
        clearTimeout(timer);
        timer = setTimeout(() => 
            fn(...args),
            t
        );
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */

/** =============== BEST SOLUTION ===============  **/

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeoutID = 0;
    
    return function(...args) {
        if (timeoutID > 0) {
            clearTimeout(timeoutID)
        }

        timeoutID = setTimeout(fn, t, ...args)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */