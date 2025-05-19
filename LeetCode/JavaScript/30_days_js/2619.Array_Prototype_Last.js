/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    if (this.length > 0) return this[this.length - 1];
    else return -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */

// ** BEST SOLUTION ** 

Array.prototype.last = function() {
    let val = this.reverse()[0];
    if ([null, 0].includes(val)) return val;
    return val || -1;
};