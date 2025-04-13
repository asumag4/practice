/*--------------------------------------------------------*/
/* Regex Validate Pin Code */

// My Answer:
function validatePIN(pin) {
  let onlyNums = /^\d+$/;
  if (pin.length === 4 || pin.length === 6) {
    if (onlyNums.test(pin)) {
      return true;
    }
    return false;
  }
  return false;
}

// Best Answer:
function validatePIN(pin) {
  return /^(\d{4}|\d{6})$/.test(pin);
}

/*--------------------------------------------------------*/
/* Friend or Foe */

// My Answer:
function friend(friends) {
  let out = [];
  let RegEx = /^[a-z]+$/i;
  for (let i = 0; i < friends.length; i++) {
    if (friends[i].length == 4 && RegEx.test(friends[i])) {
      out.push(friends[i]);
    }
  }
  return out;
}

// Best Answer:
function friend(friends) {
  return friends.filter((n) => n.length === 4);
}

/*--------------------------------------------------------*/
/* Beginner Series #1 School Paperwork */

// My Answer:
function paperwork(n, m) {
  if (n > 0 && m > 0) {
    return n * m;
  } else {
    return 0;
  }
}

// Best Answer
function paperwork(n, m) {
  return n > 0 && m > 0 ? n * m : 0;
}

/*--------------------------------------------------------*/
/* Stop gninnipS My sdroW! */

// My Answer:
function spinWords(string) {
  //TODO Have fun :)
  // Split the string into a list of strings
  const strList = string.split(" ");
  var result = [];
  // Iterate through the list of strings to:
  for (let i = 0; i < strList.length; i++) {
    let word = strList[i];
    // If 5 or more, flip the string and then concat
    if (word.length >= 5) {
      word = word.split("").reverse().join("");
    }
    // Concatenate the word
    result.push(word);
  }

  // Return the concatenated word
  return result.join(" ");
}

// Best Answer:
function spinWords(words) {
  return words
    .split(" ")
    .map(function (word) {
      return word.length > 4 ? word.split("").reverse().join("") : word;
    })
    .join(" ");
}

/*--------------------------------------------------------*/
/* Multiples of 3 or 5 */

// My Answer:
function solution(number) {
  // Create a holder list of the numbers you find that are divisble by 3 OR 5
  const holderLst = [];
  // Iterate through all numbers, from 1 to number
  for (let i = 0; i < number; i++) {
    // Find if the number is divisble by 3 OR 5
    if (i % 3 == 0) {
      // If it is add it to the list
      holderLst.push(i);
      continue;
    } else if (i % 5 == 0) {
      // If it is add it to the list
      holderLst.push(i);
      continue;
    } else {
      continue;
    }
  }
  // Sum all the numbers within the list
  const sum = holderLst.reduce((partialSum, a) => partialSum + a, 0);
  return sum;
}

// Best Answer:
function solution(number) {
  var sum = 0;

  for (var i = 1; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }
  return sum;
}
