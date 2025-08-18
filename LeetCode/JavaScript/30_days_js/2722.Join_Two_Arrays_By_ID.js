/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {

    const output = [];
    console.log("Declared 'output' variable")
    // Declare an output holder variable

    // Iterate through arr1 and append all the key:pairs into it
    console.log("Before arr1 iterations")

    console.log(arr1.length)
    for (let i = 0; i < arr1.length; i++) { 
        output[arr1[i].id] = arr1[i];
        console.log("Current iteration ID:" + arr1[i].id); // DEBUG
        console.log("Current iteration key" + arr1[i]) // DEBUG
    }

    /*
    for (let i =0; i > arr2.length; i++) {
        // If the key is already in the output array
        if (output[arr2[i].id]) {
            // Then iterate through the keys of the item and see if theres sub items that need to be replaced
            for (const key in arr2[i]) {
                output[arr2[key]] = arr2[i]; 
            }
        }
        else {
            output[arr2[i].id] = arr[i];
        }
    }
    // Iterate through arr1, and go into any sub-objects and iterate through those key:pairs
    // if it doesn't have a key:pair then return the value of the key you are on
    */
    return output;
};

const arr1 = [
    {"id": 1, "x": 1},
    {"id": 2, "x": 9}
]
const arr2 = [
    {"id": 3, "x": 5}
]
console.log(join(arr1,arr2))
