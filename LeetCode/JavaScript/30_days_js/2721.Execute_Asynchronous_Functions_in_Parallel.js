/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {

    // Init a new promise obj to be returned 
    return new Promise ( (resolve, reject)  => {

    //  Create a new array that is the Array of the lengths of the functions 
    const arr1 = new Array(functions.length);
    //  Initiate a counter at 0 
    const counter = 0;
    //  For each function in functions
    functions.forEach( (fn, i) => {
    //      initate the function
        fn().
    //      use .then() clause, where the value  is appened to your holder array at the respective index
        then( val => { 
            arr1[i] = val;
    //      iterate the counter
            counter++; 
    //      Now evaluate, if we're at the end of the functions array, resolve the results
            if (count === functions.length) resolve(results);
            };
    //      Under the .then() clause, have .catch() clause for where the reason is caught as a rejection
        ).catch(reason => reject(reason));
        });
    });
};