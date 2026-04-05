// ** MY SOLUTION **

var TimeLimitedCache = function() {
    this.cache = {};
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    // If an object exists (with key and timer), reset the object and it's value
    if (this.cache[key] && this.cache[key].timer) {
        this.cache[key].value = value;
        this.cache[key].timer = setTimeout(() => {
            this.remove(key)},
            duration)
        return true;
    } else {
    // else, the object does not exist therefore set the object with value and timer
        this.cache[key] = {
            value : value,
            timer : setTimeout(() => {
                this.remove(key)}, 
            duration)};
        return false;
    }
    
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    // Get the object via key (and if it has a valid timer) and get it's value
    if (this.cache[key] && this.cache[key].timer){
        return this.cache[key].value;
    } else {
        return -1;
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    count = 0;
    // for each key in the cache
    for (const key in this.cache) {
        // if the key has a .timer attr, then get the value
        if (this.cache[key] && this.cache[key].timer) {
            count++;
        };
    };
    return count;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */

 // Create a function of the object that can delete attributes in the cache
 TimeLimitedCache.prototype.remove = function(key) {
    delete this.cache[key];
 };

// ** BEST SOLUTION **

var TimeLimitedCache = function() {
    this.cache = {};
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const exp = Date.now() + duration;
    let currentValue, currentExpiration, isExpired = true;
    const cv = this.cache[key]
    if (cv) {
        // console.log(key)
        // console.log(this.cache)
        // console.log(this.cache[key])
        // console.log(this.cache[key][0])
        // console.log(this.cache[key][1])
        // [currentValue, currentExpiration] = cv;
        currentValue = cv[0];
        currentExpiration = cv[1];
        isExpired = Date.now() > currentExpiration;
    }
    this.cache[key] = [value, exp];
    return !isExpired;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    let currentValue, currentExpiration, isExpired = true;
    if (this.cache[key]) {
        [currentValue, currentExpiration] = this.cache[key];
        isExpired = Date.now() > currentExpiration;
    }
    return isExpired ? -1 : currentValue;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.entries(this.cache).filter(([key,tuple]) => tuple[1] > Date.now()).length;
};