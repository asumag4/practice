/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function fn(...args) {
        const executed = fn(...args);

        const timedOut = new Promise(() => {
            setTimeOut(fn(...args),t);
        });

        return Promise.race([executed, timedOut])
    };
};



// Promise.race() => https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race