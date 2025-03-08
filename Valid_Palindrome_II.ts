/*

680. Valid Palindrome II
Solved
Easy
Topics
Companies

Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false



Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.

*/

function validPalindrome(s: string): boolean {

    let i: number = 0;
    let j: number = s.length - 1;

    while (i < j) {

        if (s[i] !== s[j]) {
            const deleteI: string = s.slice(i + 1, j + 1);
            const deleteJ: string = s.slice(i, j);
            return isPalindrome(deleteI) || isPalindrome(deleteJ);
        };

        i++;
        j--;

    };

    return true;
}

function isPalindrome(s: string): boolean {
    return s === s.split('').reverse().join('');
};


// Example usage:
console.log(validPalindrome("aba"));  // Output: true
console.log(validPalindrome("abca")); // Output: true
console.log(validPalindrome("abc"));  // Output: false
