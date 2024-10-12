/*

48. Rotate Image
Solved
Medium
Topics
Companies

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]



Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

*/



import java.util.List;

class Solution1 {
    public void rotate(List<List<Integer>> matrix) {
        int n = matrix.size();

        // Transpose the matrix
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int temp = matrix.get(i).get(j);
                matrix.get(i).set(j, matrix.get(j).get(i));
                matrix.get(j).set(i, temp);
            }
        }

        // Reverse each row
        for (List<Integer> row : matrix) {
            java.util.Collections.reverse(row);
        }
    }
}

class Solution2 {
    public void rotate(List<List<Integer>> matrix) {
        int n = matrix.size();
        // Create a new matrix to store the rotated values
        List<List<Integer>> rotated = new java.util.ArrayList<>();

        for (int j = 0; j < n; j++) {
            List<Integer> newRow = new java.util.ArrayList<>();
            for (int i = n - 1; i >= 0; i--) {
                newRow.add(matrix.get(i).get(j));
            }
            rotated.add(newRow);
        }

        // Modify the original matrix in-place
        for (int i = 0; i < n; i++) {
            matrix.set(i, rotated.get(i));
        }
    }
}
