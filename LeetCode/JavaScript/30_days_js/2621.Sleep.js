// --- MY SOLUTION ---

/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}

// SOLUTION: https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep

// --- BEST SOLUTION ---

