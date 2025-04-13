var once = function(fn) {
    let counter = 0;

    return function(...args){
        counter++;
        if (counter > 1) return undefined
        else return fn(...args)
    }
};

// BASE CASE 
let fn = (a,b,c) => (a + b + c)
let onceFn = once(fn)

console.log(onceFn(1,2,3)); // 6
console.log(onceFn(2,3,6)); // returns undefined without calling fn

console.log("-----------------------------------------------")

// CASE 1 
fn = (a,b,c) => (a * b * c)
onceFn = once(fn);
console.log(onceFn(5, 7, 4)); // 140
console.log(onceFn(2, 3, 6)); // undefined, fn was not called
console.log(onceFn(4, 6, 8)); // undefined, fn was not called

// BEST SOLUTION

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let called=false
    return function(...args){
        if(!called){
            called=true;
            return fn(...args)
        }
        return undefined
    }
};