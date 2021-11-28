'''Q2. Points on same line
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two array of integers A and B describing a pair of (A[i], B[i]) coordinates in 2D plane. A[i] describe x coordinates of the ith point in 2D plane whereas B[i] describes the y-coordinate of the ith point in 2D plane.

Find and return the maximum number of points which lie on the same line.



Problem Constraints

1 <= (length of the array A = length of array B) <= 1000

-105 <= A[i], B[i] <= 105



Input Format

First argument is an integer array A.
Second argument is an integer array B.



Output Format

Return the maximum number of points which lie on the same line.



Example Input

Input 1:

 A = [-1, 0, 1, 2, 3, 3]
 B = [1, 0, 1, 2, 3, 4]
Input 2:

 A = [3, 1, 4, 5, 7, -9, -8, 6]
 B = [4, -8, -3, -2, -1, 5, 7, -4]


Example Output

Output 1:

 4
Output 2:

 2


Example Explanation

Explanation 1:

 The maximum number of point which lie on same line are 4, those points are {0, 0}, {1, 1}, {2, 2}, {3, 3}.
Explanation 2:

 Any 2 points lie on a same line.'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        N, hm = len(A), {}
        max_freq = float('-inf')

        for i in range(N):

            x1, y1 = A[i], B[i]
            dups = 0
            
            for j in range(i+1, N):

                x2, y2 = A[j], B[j]
                # Handle edge cases

                #1 duplicates
                if x1 == x2 and y1 == y2:
                    dups += 1
                
                #2 if vertical lines, slope would be infinity
                elif x1 == x2:

                    if 'inf' not in hm:
                        hm['inf'] = 1
                    else:
                        hm['inf'] += 1

                #3 Reduced slope tuple
                else:
                    num = y2 - y1
                    den = x2 - x1

                    # # If one of numerator & denominator is negative, ensure negative sign is for numerator to stay consistent with all slopes, similarly if both negative, convert to positive
                    # if (num >= 0 and den < 0) or (num < 0 and den < 0):
                    #     num, den = num * -1, den * -1
                        
                    # # Find gcd of absolute values of num and den 
                    # g = self.gcd(abs(num), abs(den))

                    #Taking gcd as is without absolute values will take care of negative signs automatically. No need for an if condition as above
                    g = self.gcd(num, den)
                    num, den = num // g, den // g

                    # Store reduced tuple in the hash map

                    if (num, den) not in hm:
                        hm[(num, den)] = 1
                    else:
                        hm[(num, den)] += 1
            
            # Iterate through hash map and find max occurence. Add duplicates and the 1 for the fixed point itself to get a candidate solution
            max_freq = max(max_freq, dups)

            for tup in hm:
                curr = hm[tup] + dups + 1
                max_freq = max(max_freq, curr)
                
            # Clear out map for next iteration by fixing the next point
            hm.clear()
            
        return max_freq

        '''
        TC: O(N^2)...fix a point and try with all others
        SC: O(N)...using a single hash map and clearing it after each iteration

        Fix a point, calculate its slope with every other point.
        Store slope in reduced form as a tuple (num, den). Take care when both num, den are negative or just one of them is negative (where to store the negative sign ??)
        Take care to handle two edge cases: duplicates in the array (just add it to final count), points forming a line || y-axis (maintain a special count for this in the hash map)
        Hash map of frequency of tuples
        Find max occurence of slope and add 1 to it. Need to specially handle duplicates
        Run for all points. O(n^2), O(N) TC, SC respectively
        Outer loop i = 0 to N, inner loop j = i + 1 to N (to avoid overcounting)
        '''
    
    def gcd(self, x, y):
        # Euclid's Algorithm
        while x:
            x, y = y % x, x
        return y