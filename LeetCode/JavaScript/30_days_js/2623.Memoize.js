function memoize(fn) {
    
    // Memoized: return a cached (saved) value for an output when the same input is ran more than once 

    /*
        Three function inputs: 
        1. sum: ordering is irrelevant, run anyways
        2. fib: if n <= 1; return 1
        3. factorial: n <= 1; return 1
    */

    const cache = new Map();


    return function(...args) {

        const args_string = JSON.stringify(args)

        // See if we have the function first
        if (cache.has(args_string)) { // If we have the function -> see if the input is cached
                return cache.get(args_string)

        } else { // If we don't have the function first cached -> create it 
            // Then generate an output and cache & return it 
            output = fn(...args)
            cache.set(args_string, output)
            return output
        }
    }
}


// BASE CASE 

let callCount = 0;
// const memoizedFn = memoize(function (a, b) {
//     callCount += 1;
//     return a + b;
// })
// console.log(memoizedFn(2, 3)) // 5
// console.log(memoizedFn(2, 3)) // 5
// console.log(callCount) // 1 

// CASE 1
const sum = (a, b) => a + b;
const memoizedSum = memoize(sum);
console.log(memoizedSum(2, 2)); // "call" - returns 4. sum() was called as (2, 2) was not seen before.
console.log(memoizedSum(2, 2)); // "call" - returns 4. However sum() was not called because the same inputs were seen before.
// "getCallCount" - total call count: 1
console.log(memoizedSum(1, 2)); // "call" - returns 3. sum() was called as (1, 2) was not seen before.
// "getCallCount" - total call count: 2
console.log(callCount)

// EDGE CASE
// const memoizedFn = memoize(function (a, b) {
//     callCount += 1;
//     return a + b;
// })
// console.log(memoizedFn(0, 0)) 
// console.log(memoizedFn(0, 0)) 
// console.log(callCount) // 1 

/* 

cache[fn] uses fn (the function reference) as a key in the cache object. 
However, JavaScript does not use string representations of functions for 
object keys—these keys are treated differently.

When you pass 0 values into fn, the logic unintentionally runs the fn 
function again even though caching is expected. This is due to discrepancies 
in how fn references are stored in cache.

*/

// BEST SOLUTION 

/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {

    //solution 2.
    const cache = new Map(); // Use a Map() object
    return function(){ 
        let key = arguments[0]; 
        if(arguments[1]){
            key += arguments[1] * 100001 // Generate unique key for an argument
        }
        const res = cache.get(key); // Retrieve value from Map() via key
        if(res !== undefined){ 
            return res;
        }
        const output = fn.apply(null, arguments); // Use .appy() instead of calling the function by itself
        cache.set(key, output); // Saving the output as value with key as key in Map()
        return output
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
