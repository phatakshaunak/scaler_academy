'''Q1. Aggressive cows
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?



Problem Constraints

2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return the largest minimum distance possible among the cows.



Example Input

Input 1:

A = [1, 2, 3, 4, 5]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 
John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
So the minimum distance will be 2.
Explanation 2:

 
The minimum distance will be 1.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        A.sort()
        # Define search space, min can be 1 or minimum difference between adjacent array elements ; max will be (max - min) // B - 1 ; We can simply choose between 1 to max constraint or 1 to max of array
        
        s = float('inf')
        
        for j in range(1,len(A)):
            
            s = min(s, (A[j] - A[j-1]))
        
        e = (A[-1] - A[0]) // (B - 1)
        
        while s <= e:
            # Here we want to check if B cows can be placed at least mid distance apart. Thus if that is satisfied, then move right, else move left
            mid = s + (e - s) // 2
            
            if self.isvalid(A, B, mid):
                ans = mid
                s = mid + 1
            
            else:
                e = mid - 1
        
        return ans
            
    def isvalid(self, A, B, m):
        
        c, d = 0, 0
        
        for i in range(1, len(A)):
            
            d = d + A[i] - A[i-1]
            
            if d >= m:
                c += 1
                d = 0
        
        return (c+1) >= B
        
        # if (c+1) < B:
        #     return False
        
        # return True
