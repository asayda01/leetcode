/*
166. Fraction to Recurring Decimal
Medium

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.



Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"



Constraints:

    -231 <= numerator, denominator <= 231 - 1
    denominator != 0



*/
class Solution {
    fractionToDecimal(numerator, denominator) {
        if (numerator === 0) return "0";

        let sign = numerator * denominator < 0 ? "-" : "";
        numerator = Math.abs(numerator);
        denominator = Math.abs(denominator);

        // Integer part
        let integer = Math.floor(numerator / denominator);
        let remainder = numerator % denominator;
        if (remainder === 0) return sign + integer.toString();

        let result = {};
        let decimal = "";
        let index = 0;

        while (remainder > 0 && !(remainder in result)) {
            result[remainder] = index;
            remainder *= 10;
            decimal += Math.floor(remainder / denominator);
            remainder %= denominator;
            index++;
        }

        if (remainder in result) {
            const repeatIndex = result[remainder];
            return sign + integer + "." + decimal.slice(0, repeatIndex) + "(" + decimal.slice(repeatIndex) + ")";
        } else {
            return sign + integer + "." + decimal;
        }
    }
}

// Test cases
const solution = new Solution();

console.log(solution.fractionToDecimal(1, 2)); // Output: "0.5"
console.log(solution.fractionToDecimal(4, 333)); // Output: "0.(012)"
console.log(solution.fractionToDecimal(2, 1)); // Output: "2"
