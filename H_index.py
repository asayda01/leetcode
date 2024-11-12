"""

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.



Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1



Constraints:

    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000

"""

from typing import List


class Solution:

    def hIndex(self, citations: List[int]) -> int:

        len_citations = len(citations)
        temp_cit = [0] * (len_citations + 1)
        count_cit = 0

        for index_i, element in enumerate(citations):

            if element > len_citations:
                temp_cit[len_citations] += 1

            else:
                temp_cit[element] += 1

        for index_j in range(len_citations, -1, -1):
            count_cit += temp_cit[index_j]

            if count_cit >= index_j:
                return index_j


class Solution:

    def hIndex(self, citations: List[int]) -> int:

        len_citations = len(citations)
        citations.sort()

        for index, element in enumerate(citations):
            if len_citations - index <= element:
                return len_citations - index

        return 0


citations_1 = [1, 3, 1]
print(Solution().hIndex(citations_1))

citations_2 = [3, 0, 6, 1, 5]
print(Solution().hIndex(citations_2))
