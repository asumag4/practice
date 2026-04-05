// ** SOLUTION **

var expect = function(val) {
    return {
         toBe:  (toBeVla) => {
            if (val === toBeVla) return true
            else throw new Error("Not Equal")
        },
        notToBe: (notToBeVal) => {
            if(val  !== notToBeVal) return true
            else throw new Error("Equal")
        }
    }
};