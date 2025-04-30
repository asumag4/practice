/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    
    // Handling None
    if (arr.length < 1) {
        return []
    }

    // Initialize a counter outside the for loop first
    let counter = 0;
    // Initialize an output array outside the for loop 
    let out = [];
    let chunk_handler = []; 

    // Have a for loop that iterates through the entire arr
    for (let elem of arr) { 

        chunk_handler.push(elem);
        counter++;

        // Increment the counter each loop, when we get to the size, reset the counter and append your chunked array
        if (counter >= size) {
            out.push(chunk_handler)
            // Reset everything 
            chunk_handler = [];
            counter = 0;
        }
    
    }

    // If theres still stuff in chunk_handler... 
    if (chunk_handler.length >= 1) {
        out.push(chunk_handler)        
    }

    return out;
};

// --- BEST SOLUTION ---

var chunk = function(arr, size) {

    if (arr.length === 0) { // None handling
        return arr;
    }

    let newArr = []; 
    let i = 0;
    let n = arr.length
 
    while (i < n) {  // Going through the array through position rather than per every element
        newArr.push(arr.slice(i, i+size)); // Using slices instead of building new `chunk` arrays
        i += size;
    }

    return newArr;
};

// --- TEST CASES --- 

console.log(chunk([1,2,3,4,5],1)) // [[1],[2],[3],[4],[5]]
console.log(chunk([1,2,3,4,5],3)) // [[1,9,6],[3,2]]
// If we reach the end of the list without anything in out; place in chunk_handler 
console.log(chunk([8,5,3,2,6],6)) // [[8,5,3,2,6]]
console.log(chunk([],1)) // # 
// Another case: If theres left over, place it into the chunk, this can be ammended with the base 
console.log(chunk(["1","2","3","4","5"],2))
