// MY SOLUTION 

var reduce = function(nums, fn, init) {
    const outArr = [];
    // Take care of the first case 
    let val = fn(init,nums[0]);
    // Take care of the rest
    if (nums.length != 0) { 
        for (let i = 1; i < nums.length; i++) {
            val = fn(val, nums[i])
        }
        return val;
    }
    return init;
};

// ** BEST SOLUTION ** 
var reduce = function(nums, fn, init) {
    let val = init;
    for(let i=0;i< nums.length;i++){
      val = fn(val, nums[i]);
     
    }
        return val;
};

/* 

NOTE: I was trying to 'hack' my way through by skipped test case 0;
but what if there were no objs in the array? You should always start 
from 0 then! Lesson learned. 

*/

