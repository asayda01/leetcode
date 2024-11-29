"""

219. Contains Duplicate II
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false



Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105


"""

from typing import List


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic = {}

        for index, element in enumerate(nums):

            if element in dic and index - dic[element] <= k:
                return True

            dic[element] = index

        return False

# nums_1 = [1,2,3,1]
# k_1 = 3
# print(Solution().containsNearbyDuplicate(nums_1, k_1))


# nums_2 = [1,0,1,1]
# k_2 = 1
# print(Solution().containsNearbyDuplicate(nums_2, k_2))


# nums_3 = [1,2,3,1,2,3]
# k_3 = 2
# print(Solution().containsNearbyDuplicate(nums_3, k_3))
