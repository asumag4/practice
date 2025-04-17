// MY SOLUTION 

var map = function(arr, fn) {
    let outArr = [];
    arr.forEach((elem, i) => outArr.push(fn(elem, i)));
    return outArr;
};

// ** BEST SOLUTION ** 

var map = function(arr, fn) {
    const newArr = []; 
    for(let i = 0; i < arr.length; i++){
        newArr.push(fn(arr[i], i))
    }
    return newArr
};

/* 

The major reason why my previous solution wouldn't work: 

var map = function(arr, fn) {
    let outArr = [];
    for (let i = 0; i < arr.length; i++) {
        outArr.push(fn(arr[i], i));
    }
    return outArr;
};

Is because I was using `.len` to get the length of the array, 
where I should've been using `.length`

*/
