/**
 * @param {number} n
 * @return {string}
 */
let countAndSay = function(n) {
    if (n === 1) {
        return "1";
    } else {
        let prevSeq = countAndSay(n - 1);
        let result = "";
        let count = 1;

        for (let i = 0; i < prevSeq.length; i++) {
            if (prevSeq[i] === prevSeq[i + 1]) {
                count++;
            } else {
                result += count + prevSeq[i];
                count = 1;
            }
        }

        return result;
    }
};

// Generate the count-and-say sequence for the first 5 numbers
for (let i = 1; i <= 5; i++) {
    console.log("Count-and-Say (" + i + "): " + countAndSay(i));
}