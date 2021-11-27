'''Q3. When will the ants die
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

We have a wooden plank of the length A units. Some ants are walking on the plank, each ant moves with speed 1 unit per second. Some of the ants move to the left, the other move to the right.
When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions doesn't take any additional time.

When an ant reaches one end of the plank at a time t, it falls out of the plank imediately.

Given an integer A and two integer arrays B signifying left going ants and C signifying right going ants, the positions of the ants moving to the left and the right. Return the moment when the last ant(s) fall out of the plank.





Problem Constraints

1 <= A <= 10^4
0 <= B.length <= A + 1
0 <= B[i] <= A
0 <= C.length <= A + 1
0 <= C[i] <= A
1 <= B.length + C.length <= A + 1
All values of left and right are unique, and each value can appear only in one of the two arrays.


Input Format

First argument contains integer A.

Second argument contains B denoting ants moving left.

Third argument contains C denoting ants moving right.


Output Format

Return a single integer.


Example Input

Input 1:
n = 4
left = [4,3]
right = [0,1]

Input 2:

n = 9
left = [5]
right = [4]


Example Output

Output 1:
4

Output 2:

5


Example Explanation

Explanation 1:
In the image above:
-The ant at index 0 is named A and going to the right.
-The ant at index 1 is named B and going to the right.
-The ant at index 3 is named C and going to the left.
-The ant at index 4 is named D and going to the left.
Note that the last moment when an ant was on the plank is t = 4 second, after that it falls imediately out of the plank. (i.e. We can say that at t = 4.0000000001, there is no ants on the plank).
Explaination 2

At t = 1 second, both ants will be at the same intial position but with different direction.'''

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        if not B:
            return A - min(C)
        
        if not C:
            return max(B)
        
        left = max(B)
        right = min(C)
        
        return max(left, A - right)

#Time O(len(B) + len(C)), Space O(1)