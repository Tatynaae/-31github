/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filteredArr = [];

  for (let i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      filteredArr.push(arr[i]);
    }
  }

  return filteredArr;
};


// Example usage:
const arr = [1, 2, 3, 4, 5];
const isEven = (num) => num % 2 === 0;

const filteredArr = customFilter(arr, isEven);
console.log(filteredArr); // Output: [2, 4]