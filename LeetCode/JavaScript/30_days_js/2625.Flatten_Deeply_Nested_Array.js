/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {

    // Get an array and hierarchy level of all the items in your array
    const digestedArr = [...arr.map(item => [item, n])];
    //console.log(digestedArr);
    
    // Set an empty array as an output that will be inputted when the depth = 0 for each item
    const output = [];

    // Iterate through this digested array while there are still stuff in it
    while (digestedArr.length > 0){   
        // Use a for loop to iterate through the items in digestArr
        for (let i = 0; i < digestedArr.length; i++) {

            // Take out an item and work on that for each iteration 
            let popout = digestedArr[i];

            // If depth > 0 AND the item in the array can be further broken down
            if (Array.isArray(popout) && (popout[1] > 0)){
                // Then break it down
                popout = [...popout.map([subItem, subN] => [subItem, subN - 1])];
                // And then reset the item in digestedArr
                digestedArr.splice(i, 1, ...popout);
            } else {
                // If the depth = 0, then append this item
                output.push(digestedArr[i].pop());
            }
        };
    };
    // Return the output 
};