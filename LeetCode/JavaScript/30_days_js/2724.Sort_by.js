// *** MY ATTEMPTS ***

// This is the correct answer
/*
var sortBy = function(arr, fn) {
    return arr.toSorted((a,b) => fn(a) - fn(b));
};
*/

/*
var sortBy = function(arr, fn) {
    return arr.toSorted((a,b) => fn(b) - fn(a));
};


var sortBy = function(arr, fn) {
    return arr.sort(function(a,b){
        fn(b) - fn(a)
    })
}

var sortBy = function(arr, fn) {
    return arr.toSorted(function(a,b){
        fn(b) - fn(a)
    })
}
*/

// *** Also correct answer && BEST ANSWER ***
var sortBy = function(arr, fn) {
    return arr.sort(function(a,b){
        return fn(a) - fn(b)
    })
}


