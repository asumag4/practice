// ** MY SOLUTION **

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
// 1. Iterate through items in Array
    const out = {};
    for (let i=0; i<this.length;i++) {
        // console.log("Current Item: "); // DEBUG
        // console.log(this[i]) // DEBUG
        id = fn(this[i]);
        if (out.hasOwnProperty(id)) {
            out[id].push(this[i])
        } 
        else {
            // console.log("Appending new ID log;") // DEBUG
            console.log(id) // DEBUG
            out[id] = [];
            out[id].push(this[i]);
        }
        // console.log("Current state of output: ") // DEBUG
        // console.log(out); // DEBUG
    }
    return out

// 2. Use the function to return the object key we need 
// 3. If the ID exists in the return obj, append the object_i, if not then make a new key and then append object_i 
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

// ** BEST SOLUTION ** 

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    group = {}
    for(let i=0; i<this.length; i++){
        let key = fn(this[i]);
        let arr = group[key];

        if(!arr){
            arr = []  
            group[key] = arr;  // group[key] points to arr   
        }
        
        arr.push(this[i])  // hence pushing to arr works or you can also push to group[key] .
    }
    return group;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */