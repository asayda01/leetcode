/*
** Instructions to candidate.
**  1) You are an avid rock collector who lives in southern California. Some rare
**     and desirable rocks just became available in New York, so you are planning
**     a cross-country road trip. There are several other rare rocks that you could
**     pick up along the way.
**
**     You have been given a grid filled with numbers, representing the number of
**     rare rocks available in various cities across the country.  Your objective
**     is to find the optimal path from So_Cal to New_York that would allow you to
**     accumulate the most rocks along the way.
**
**     Note: You can only travel either north (up) or east (right).
**  2) Consider adding some additional tests in doTestsPass().
**  3) Implement optimalPath() correctly.
**  4) Here is an example:
**                                                           ^
**                 {{0,0,0,0,5}, New_York (finish)           N
**                  {0,1,1,1,0},                         < W   E >
**   So_Cal (start) {2,0,0,0,0}}                             S
**                                                           v
**   The total for this example would be 10 (2+0+1+1+1+0+5).
*/


public class RockCollector {

    public static int optimalPath(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int rows = grid.length;
        int cols = grid[0].length;

        // Memoization table to store maximum rocks collected at each position
        int[][] memo = new int[rows][cols];

       for(int[] m : memo){
          Arrays.fill(m,-1);
       }

        // Start recursive call from the bottom-left corner (So_Cal)
        return collectMaxRocks(grid, rows - 1, 0, memo);
    }

    private static int collectMaxRocks(int[][] grid, int row, int col, int[][] memo) {
         // Destination check: If we're at the top-right corner (New York)
        if (row == 0 && col == grid[0].length - 1) {
            return grid[row][col];  // Return the number of rocks at the destination
        }

        // Base case: if we are out of bounds, return 0 rocks
        if (row < 0 || col < 0) {
            return 0;
        }

        // If the result is already computed, return it from the memo table
        if (memo[row][col] != -1) {
            return memo[row][col];
        }

        int rocksFromLeft = collectMaxRocks(grid, row, col - 1, memo);
        int rocksFromBelow = collectMaxRocks(grid, row - 1, col, memo);

        memo[row][col] = grid[row][col] + Math.max(rocksFromLeft, rocksFromBelow);

        return memo[row][col];
    }
}

