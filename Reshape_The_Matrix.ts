/*
566. Reshape the Matrix
Solved
Easy
Topics
Companies
Hint

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]



Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    -1000 <= mat[i][j] <= 1000
    1 <= r, c <= 300


*/



function matrixReshape(mat: number[][], r: number, c: number): number[][] {

  const nums: number[] = ([] as number[]).concat(...mat);
  if (r * c !== nums.length) return mat;

  const result: number[][] = [];
  while (r--) {
    result.push(nums.slice(result.length * c, result.length * c + c));
  }
  return result;
}

// Example usage
const mat: number[][] = [[1, 2], [3, 4]];
const r: number = 4;
const c: number = 1;

console.log(matrixReshape(mat, r, c));
