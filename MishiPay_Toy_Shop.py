"""

QUESTION:

Toy shop
There are N shops present on a number line, where each shop is located at x, coordinate and has toys, number of toys in it.
You are present at point P initially and can move at most k steps.
Whenever you reach a shop, you get all the toys present in that shop.
Task
Determine the maximum toys you can gather after moving at most k steps.
Notes
• You can change your direction in between.
• No shop is present at the initial point.
• No two shops can have the same coordinates.
• You cannot buy more from a shop you already visited.
Hint. Avoid changing directions too many times.
Example

Assumptions
• T=1
• N=3
• P=0
• k=9
• x = [-9, -7, 1]
• toys = [9, 1, 10]

Approach
• Since you start at coordinate 0 and you can only move 9 steps, you are only left with two
good choices. Either you move to the left till -9, or first move to the right till 1 and then reverse the direction to go till -7. You cannot go to -9 in the latter choice as your steps are exhausted [0 -> 1(1 steps), 1-> -7 (8 steps)].
• If you move to -9 from 0, you collect (1+9)= 10 toys.
• You move from 0 to 1/1 step) and then to -7(8 steps), you collect (10 + 1) = 11 toys.
Hence in at most 9 steps, you can get a maximum of 11 toys.
Function description
Function description
Complete the function getMaxToys provided in the editor. This function takes the following 5 parameters and returns the required answer:
• N. Represents the number of shops
• P. Represents the initial position
• k. Represents the maximum number of steps you can take
• x. Represents the array containing the coordinates of each shop
• toys: Represents the array containing the number of toys present in each shop


Input format
Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).
• The first line contains 7 denoting the number of test cases. T also specifies the number of times you have to run the getMaxToys function on a different set of inputs.
• For each test case:
• The first line contains three space-separated integers N denoting the number of
shops, P denoting the initial point, k denoting the maximum number of steps, respectively.
• The second line contains N space-separated values denoting the xi of each shop.
• The third line contains N space-separated values denoting the toysi of each shop
Output format
For each test case in a new line, print the maximum number of toys.


Constraints
1≤T≤ 20
1 ≤ N ≤ 105
-106 < ;, P≤ 106
1≤ k ≤1012
1 ≤ toys; ≤ 109
Code snippets (also called starter code/boilerplate code)
This question has code snippets for Python.

Sample Input 1

1
4 0 4
-5 -125
10 2 3 4

Sample Output 1
5


Given
• T=1
• N=4
• P=0
• k = 4
• x=[-5, -1, 2, 5]
• toys [10, 2, 3, 4]


Approach
• Initially, you start at coordinate O and can move at most 4 steps. It can be noticed that you cannot reach -5 or 5. So the optimal move should be reaching the shops at -1 and 2.
• If you start moving to shop at coordinate 2, you will use 2 steps, then to -1 will take 3 steps making a total of 5 steps, hence you could not be able to take 3 toys at the shop present on coordinate 2.
• If you first started towards shop at -1, it would take 1 step, and then shop at 2 would take 3 steps making a total of 4 steps, hence you are able to take (2+3)= 5 toys.
Hence, the maximum number of toys can take is 5.


Sample Input 2


5
10 9 15
-18 -6 -1 1 7 11 12 16 17 20
77 50 73 86 57 50 6 27 91 76
10 -13 8
-1918 -12 -11 -9 -6 -3 4 12 19
46 73 77 32 77 76 14 21 46 16
10 -19 35

Sample output 2

307
262
517
64
497


"""


"""

ANSWER :

To solve this problem, we need to determine the maximum number of toys that can be collected by moving at most `k` steps from an initial position `P` on a number line, where each shop is located at a specific coordinate and contains a certain number of toys. The key is to explore all possible paths within the step limit and choose the one that maximizes the toy collection.

### Approach

1. **Sort the Shops**: First, sort the shops based on their coordinates. This helps in systematically exploring the shops in both directions (left and right) from the initial position.

2. **Prefix Sums**: Compute prefix sums for the toys from the left and right. This allows us to quickly calculate the total toys collected when moving in a particular direction.

3. **Explore Paths**: Iterate over possible paths where you move to a certain number of shops to the left and then to the right (or vice versa), ensuring that the total steps do not exceed `k`.

4. **Calculate Maximum Toys**: For each valid path, calculate the total toys collected and keep track of the maximum value.

### Solution Code

```python
def getMaxToys(N, P, k, x, toys):
    # Combine x and toys into a list of tuples and sort based on x
    shops = sorted(zip(x, toys), key=lambda shop: shop[0])
    
    # Separate the sorted x and toys
    sorted_x = [shop[0] for shop in shops]
    sorted_toys = [shop[1] for shop in shops]
    
    # Find the index where P would be inserted to keep the list sorted
    # This helps in dividing the shops into left and right of P
    left_shops = []
    right_shops = []
    for shop in shops:
        if shop[0] < P:
            left_shops.append(shop)
        else:
            right_shops.append(shop)
    
    # Prepare prefix sums for left and right shops
    # Left shops are in reverse order (closest to P first)
    left_prefix = []
    total = 0
    for shop in reversed(left_shops):
        total += shop[1]
        left_prefix.append(total)
    
    right_prefix = []
    total = 0
    for shop in right_shops:
        total += shop[1]
        right_prefix.append(total)
    
    max_toys = 0
    
    # Try all possible combinations of left and right shops
    # i is the number of left shops visited, j is the number of right shops visited
    for i in range(len(left_prefix) + 1):
        for j in range(len(right_prefix) + 1):
            if i == 0 and j == 0:
                continue  # No shops visited
            # Calculate steps
            steps = 0
            if i > 0:
                steps += abs(P - left_shops[-i][0])
            if j > 0:
                steps += abs(P - right_shops[j-1][0])
            if i > 0 and j > 0:
                steps += abs(left_shops[-i][0] - right_shops[j-1][0])
            if steps <= k:
                total_toys = (left_prefix[i-1] if i > 0 else 0) + (right_prefix[j-1] if j > 0 else 0)
                if total_toys > max_toys:
                    max_toys = total_toys
    return max_toys

# Example usage:
T = int(input())
for _ in range(T):
    N, P, k = map(int, input().split())
    x = list(map(int, input().split()))
    toys = list(map(int, input().split()))
    print(getMaxToys(N, P, k, x, toys))
```

### Explanation

1. **Sorting**: The shops are sorted based on their coordinates to facilitate easy traversal.
2. **Prefix Sums**: Prefix sums are calculated for both left and right shops to quickly determine the total toys collected up to any point.
3. **Path Exploration**: The nested loops iterate over all possible combinations of visiting shops to the left and right of the initial position. For each combination, the total steps are calculated, and if they are within the limit `k`, the total toys collected are computed.
4. **Maximization**: The maximum number of toys collected across all valid paths is tracked and returned.

This approach ensures that we consider all possible paths within the step limit and efficiently compute the maximum toys that can be collected.

"""



# CODE:


def getMaxToys(N, P, k, x, toys):
    # Combine x and toys into a list of tuples and sort based on x
    shops = sorted(zip(x, toys), key=lambda shop: shop[0])
    
    # Separate the sorted x and toys
    sorted_x = [shop[0] for shop in shops]
    sorted_toys = [shop[1] for shop in shops]
    
    # Find the index where P would be inserted to keep the list sorted
    # This helps in dividing the shops into left and right of P
    left_shops = []
    right_shops = []
    for shop in shops:
        if shop[0] < P:
            left_shops.append(shop)
        else:
            right_shops.append(shop)
    
    # Prepare prefix sums for left and right shops
    # Left shops are in reverse order (closest to P first)
    left_prefix = []
    total = 0
    for shop in reversed(left_shops):
        total += shop[1]
        left_prefix.append(total)
    
    right_prefix = []
    total = 0
    for shop in right_shops:
        total += shop[1]
        right_prefix.append(total)
    
    max_toys = 0
    
    # Try all possible combinations of left and right shops
    # i is the number of left shops visited, j is the number of right shops visited
    for i in range(len(left_prefix) + 1):
        for j in range(len(right_prefix) + 1):
            if i == 0 and j == 0:
                continue  # No shops visited
            # Calculate steps
            steps = 0
            if i > 0:
                steps += abs(P - left_shops[-i][0])
            if j > 0:
                steps += abs(P - right_shops[j-1][0])
            if i > 0 and j > 0:
                steps += abs(left_shops[-i][0] - right_shops[j-1][0])
            if steps <= k:
                total_toys = (left_prefix[i-1] if i > 0 else 0) + (right_prefix[j-1] if j > 0 else 0)
                if total_toys > max_toys:
                    max_toys = total_toys
    return max_toys

# Example usage:
T = int(input())
for _ in range(T):
    N, P, k = map(int, input().split())
    x = list(map(int, input().split()))
    toys = list(map(int, input().split()))
    print(getMaxToys(N, P, k, x, toys))