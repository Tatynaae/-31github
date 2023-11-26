/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const result = [];

    while (matrix.length > 0) {
        // Traverse top row
        result.push(...matrix.shift());

        // Traverse right column
        if (matrix.length && matrix[0].length) {
            for (let i = 0; i < matrix.length; i++) {
                result.push(matrix[i].pop());
            }
        }

        // Traverse bottom row
        if (matrix.length && matrix[0].length) {
            result.push(...matrix.pop().reverse());
        }

        // Traverse left column
        if (matrix.length && matrix[0].length) {
            for (let i = matrix.length - 1; i >= 0; i--) {
                result.push(matrix[i].shift());
            }
        }
    }

    return result;
};