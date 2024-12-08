"""
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



"""


class Solution:

    def fractionToDecimal(self, numerator, denominator):

        num, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        integer = sign + str(num)
        if remainder == 0: return integer

        result = {}
        decimal = ''
        index = 0

        while remainder > 0 and remainder not in result:
            result[remainder] = index
            num, remainder = divmod(remainder * 10, abs(denominator))
            decimal += str(num)
            index += 1

        if remainder in result:
            index = result[remainder]
            return integer + '.' + decimal[:index] + '(' + decimal[index:] + ')'

        else:
            return integer + '.' + decimal[:]


numerator = 1
denominator = 2

print(Solution().fractionToDecimal(numerator, denominator))

numerator = 4
denominator = 333
print(Solution().fractionToDecimal(numerator, denominator))
