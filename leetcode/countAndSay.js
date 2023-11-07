/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if (n === 1) {
        return "1";
    } else {
        var prevSeq = countAndSay(n - 1);
        var result = "";
        var count = 1;

        for (var i = 0; i < prevSeq.length; i++) {
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
for (var i = 1; i <= 5; i++) {
    console.log("Count-and-Say (" + i + "): " + countAndSay(i));
}