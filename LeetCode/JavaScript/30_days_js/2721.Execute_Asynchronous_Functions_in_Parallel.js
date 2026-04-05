/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise ( (resolve, reject ) => {
        const results = new Array(functions.length);
        let counter = 0;

        functions.forEach( (fn, i) => {
            fn()
            .then( val => {
                results[i] = val;
                counter++;
                if (counter == functions.length) resolve(results);
            })
            .catch(reason => reject(reason))
        })
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */