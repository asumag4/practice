/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {

    const stacked = [...arr.map(item => [item, n])];
    const output = [];

    while (stacked.length > 0) {
        const [item, n] = stacked.pop()

        if (Array.isArray(item) && n > 0) {
            stacked.push(...item.map(subItem => [subItem, n - 1]));
        } else {
            output.push(item);
        }
    }

    return output.reverse()

};

// ============ BEST SOLUTION ============

const flat = (arr, n) => arr.flat(n);