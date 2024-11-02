"""

128. Longest Consecutive Sequence
Solved
Medium
Topics
Companies

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9



Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109


"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:

            # Only check for a new sequence if it's start of a new sequence
            if num - 1 not in num_set:

                curr_num = num
                curr_long = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_long += 1

                longest = max(curr_long, longest)

        return longest


nums = [1, 2, 0, 1]

a = Solution.longestConsecutive(nums)

print(a)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, longest = set(nums), 0
        for num in s:
            if num - 1 in s: continue
            j = 1
            while num + j in s: j += 1
            longest = max(longest, j)
        return longest
