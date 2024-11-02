"""

3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint

Given a string s, find the length of the longest
substring
without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_index = {}
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length


s = "aab"

a = Solution.lengthOfLongestSubstring(s)

print(a)


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        seen = {}
        output = 0

        for right, curr in enumerate(s):
            if curr in seen:
                left = max(left, seen[curr] + 1)
            output = max(output, right - left + 1)
            seen[curr] = right

        return output
