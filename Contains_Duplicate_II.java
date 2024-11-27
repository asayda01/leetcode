/**

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


**/

class Solution {

    public boolean containsNearbyDuplicate(int[] nums, int k) {

        Set<Integer> set = new HashSet<Integer>();

        for(int i = 0; i < nums.length; i++){

            // remove element if its distance to nums[i] is not lesser than k
            if(i > k) set.remove(nums[i-k-1]);

            // because all still existed elements is closer than k distance to the num[i],
            // therefore if the add() return false,
            // it means there's a same value element already existed within the distance k,
            // therefore return true.
            if(!set.add(nums[i])) return true;

        };
        return false;

 };

};
