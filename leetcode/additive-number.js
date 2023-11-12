function isAdditiveNumber(s) {
    function isValid(num1, num2, remaining) {
        if (remaining.length === 0) {
            return true;
        }

        const sum = (BigInt(num1) + BigInt(num2)).toString();
        if (remaining.startsWith(sum)) {
            return isValid(num2, sum, remaining.slice(sum.length));
        } else {
            return false;
        }
    }

    const length = s.length;
    for (let i = 1; i < length / 2 + 1; i++) {
        for (let j = i + 1; j < length; j++) {
            const num1 = s.slice(0, i);
            const num2 = s.slice(i, j);

            if ((num1.length > 1 && num1[0] === '0') || (num2.length > 1 && num2[0] === '0')) {
                continue;  // Invalid leading zeros
            }

            if (isValid(num1, num2, s.slice(j))) {
                return true;
            }
        }
    }

    return false;
}

// Example usage:
const s1 = "112358";
const s2 = "199100199";
console.log(isAdditiveNumber(s1));  // Output: true
console.log(isAdditiveNumber(s2));  // Output: true
