/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (!digits || digits.length === 0) {
        return [];
    }

    // Define the mapping of digits to letters
    const digitMapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    };

    function backtrack(index, current) {
        if (index === digits.length) {
            result.push(current);
            return;
        }

        const letters = digitMapping[digits[index]];
        for (const letter of letters) {
            backtrack(index + 1, current + letter);
        }
    }

    const result = [];
    backtrack(0, '');

    return result;
};