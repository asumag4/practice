// MY SOLUTION

var filter = function(arr, fn) {
    const outArr = [];
    for (let i = 0; i < arr.length; i++) {
      if (fn(arr[i], i)) {
          outArr.push(arr[i]);
      } else {
          continue;
      }
    }  
    return outArr;
};

// ** BEST SOLUTION ** 

var filter = function(arr, fn) {
    let fil=[]
    for(let i=0;i<arr.length;i++){
        if(fn(arr[i],i)){
            fil.push(arr[i]);
        }
    }
    return fil
};

/* 

We can make do without the `else{}` clause

*/