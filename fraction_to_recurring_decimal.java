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
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        // Handle case when numerator is 0
        if (numerator == 0) return "0";

        // Determine the sign of the result
        StringBuilder result = new StringBuilder();
        if (numerator < 0 ^ denominator < 0) {
            result.append('-');
        }

        // Use absolute values
        long num = Math.abs((long) numerator); // Use long to avoid overflow
        long denom = Math.abs((long) denominator);

        // Get the integer part
        result.append(num / denom);
        long remainder = num % denom;
        if (remainder == 0) return result.toString(); // Return if there is no decimal part

        result.append('.'); // Begin decimal part

        Map<Long, Integer> remainderMap = new HashMap<>();
        int index = result.length(); // Store starting index of decimal part

        // Process the fractional part
        while (remainder != 0) {
            // If we have seen this remainder before, we have a repeating decimal
            if (remainderMap.containsKey(remainder)) {
                int startIndex = remainderMap.get(remainder);
                result.insert(startIndex, '('); // Insert "(" at the start of the repeat
                result.append(')'); // Append ")" at the end of the repeat
                return result.toString();
            }

            // Map the remainder to its index in the result string
            remainderMap.put(remainder, index++);
            remainder *= 10;
            result.append(remainder / denom); // Append the next digit
            remainder %= denom; // Update the remainder
        }

        return result.toString(); // Return the final result
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test cases
        int numerator1 = 1;
        int denominator1 = 2;
        System.out.println(solution.fractionToDecimal(numerator1, denominator1)); // Output: "0.5"

        int numerator2 = 2;
        int denominator2 = 1;
        System.out.println(solution.fractionToDecimal(numerator2, denominator2)); // Output: "2"

        int numerator3 = 4;
        int denominator3 = 333;
        System.out.println(solution.fractionToDecimal(numerator3, denominator3)); // Output: "0.(012)"
    }
}
