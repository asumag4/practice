// ** MY SOLUTION **

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function fn(...args) {
        const executed = fn(...args);

        const timedOut = new Promise(() => {
            setTimeOut(fn(...args),
            t);
        })

        return Promise.race([executed, timedOut])
    };
};

// ** BEST SOLUTION **
var timeLimit = function(fn, t) {
    return async function(...args) {
        return new Promise((resolve, reject) => {
            const tid = setTimeout(() => {
                reject("Time Limit Exceeded")
            }, t)
            fn(...args).then((o) => {
                clearTimeout(tid)
                resolve(o)
            }).catch((err) => {
                clearTimeout(tid)
                reject(err)
            })
        })
    }
};

// Promise.race() => https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race