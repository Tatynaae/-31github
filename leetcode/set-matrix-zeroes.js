/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
        return;
    }

    const rows = matrix.length;
    const cols = matrix[0].length;
    const zeroRows = new Set();
    const zeroCols = new Set();

    // Mark rows and columns that contain 0
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (matrix[i][j] === 0) {
                zeroRows.add(i);
                zeroCols.add(j);
            }
        }
    }

    // Set 0 for marked rows
    zeroRows.forEach(row => {
        for (let j = 0; j < cols; j++) {
            matrix[row][j] = 0;
        }
    });

    // Set 0 for marked columns
    zeroCols.forEach(col => {
        for (let i = 0; i < rows; i++) {
            matrix[i][col] = 0;
        }
    });
};

// console.log(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))/