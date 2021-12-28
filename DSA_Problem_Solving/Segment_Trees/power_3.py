'''Q2. Power of 3
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary string A of size N and an integer matrix B of size Q x 3.

Matrix B has Q queries:

For queries of type B[i][0] = 1, flip the value at index B[i][1] in A if and only if the value at that index is 0 and return -1.
For queries of type B[i][0] = 0, Return the value of the binary string from index B[i][1] to B[i][2] modulo 3.
Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

1 <= N <= 100000
1 <= Q <= 200000
1 <= B[i][1], B[i][2] <= N
B[i][1] <= B[i][2]



Input Format

The first argument given is the string A.
The second argument given is the integer matrix B of size Q * 3.



Output Format

Return an array of size Q where ith value is answer to ith query.



Example Input

Input 1:

 A = 10010
 B = [  [0, 3, 5]
        [0, 3, 4]
        [1, 2, -1]
        [0, 1, 5]
     ]
Input 2:

 A = 11111
 B = [
        [0, 2, 4]
        [1, 2, -1
        [0, 2, 4]]
     ]


Example Output

Output 1:

 [2, 1, -1, 2]
Output 2:

 [1, -1, 1]


Example Explanation

Explanation 1:

 For query 1, binary string from index 3 to 5 is 010 = 2. So 2 mod 3 = 2.
 For query 2, binary string from index 3 to 4 is 01 = 1. So 1 mod 3 = 1.
 After query 3, given string changes to 11010.
 For query 4, binary string from index 1 to 5 is 11010 = 26. So 26 mod 3 = 2.
 So, output array is [2, 1, -1, 2].
Explanation 2:

 For query 1, binary string from index 2 to 4 is 111 = 7. So 7 od 3 = 1.
 After query 2, string remains same as there is already 1 at index 2.
 For query 3, binary string from index 2 to 4 is 111 = 7. So 7 od 3 = 1.
 So, output array is [1, -1, 1].'''

class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        n = len(A)

        T = [0] * (4 * n)

        self.build(0, n-1, 0, T, A)
        ans = []
        for i in range(len(B)):
            a, b, c = B[i]

            if a == 1:
                ans.append(c)
                self.update(0, n - 1, 0, b - 1, T, A)
            
            else:
                curr = self.query(0, n - 1, 0, b - 1, c - 1, T, A)
                ans.append(curr % 3)
        
        return ans
        
    def build(self, s, e, idx, T, A):

        if s == e:
            
            T[idx] = int(A[s])
            return
        
        mid = s + (e - s) // 2

        l_c = (2 * idx) + 1
        r_c = l_c + 1

        self.build(s, mid, l_c, T, A)
        self.build(mid + 1, e, r_c, T, A)
        
        T[idx] = (T[l_c] << (e - mid)) + T[r_c]
    
    def update(self, s, e, idx, idx1, T, A):
        
        if s == e:
            if T[idx] == 0:
                T[idx] = 1
                
            return
        
        mid = s + (e - s) // 2

        l_c = 2 * idx + 1
        r_c = l_c + 1

        if idx1 <= mid:
            self.update(s, mid, l_c, idx1, T, A)
        
        else:
            self.update(mid + 1, e, r_c, idx1, T, A)

        T[idx] = (T[l_c] << (e - mid)) + T[r_c]        
    
    def query(self, s, e, idx, L, R, T, A):

        # Three cases, complete overlap, partial overlap and no overlap

        # Complete overlap
        if s >= L and e <= R:
            return T[idx]
        
        # No overlap
        if L > e or R < s:
            return 0
        
        # Partial overlap
        mid = s  + (e - s) // 2

        l_c = 2 * idx + 1
        r_c = l_c + 1

        left = self.query(s, mid, l_c, L, R, T, A)
        right = self.query(mid + 1, e, r_c, L, R, T, A)

        bits = min(e-mid, R - mid)
        bits = max(0, bits)

        return (left << (bits)) + right