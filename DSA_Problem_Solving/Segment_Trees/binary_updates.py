'''Q3. Binary updates
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A denoting the size of the array consisting all ones.

You are given Q queries, for each query there are two integer x and y:

If x is 0, then update the value of array at index y to 0.
If x is 1, then output the index of yth one in the array. If there is no such index then output -1.
NOTE 1: There will atleast 1 query where value of x is 1.



Problem Constraints

1 <= A, Q <= 105

0 <= x <= 1

1 <= y <= A



Input Format

First argument is an integer A denoting the size of array.

Second argument is a 2-D array B of size Q x 2 where B[i][0] denotes x and B[i][1] denotes y.



Output Format

Return an integer array denoting the output of each query where x is 1.



Example Input

Input 1:

 A = 4
 B = [ [1, 2],
       [0, 2],
       [1, 4] ]
Input 2:

 A = 5
 B = [ [0, 3],
       [1, 4],
       [0, 3],
       [1, 5] ] 


Example Output

Output 1:

 [2, -1]
Output 2:

 [5, -1]


Example Explanation

Explanation 1:

 Initially array = [1, 1, 1, 1]. For first query 2nd one is at index 2.
 After Second query array becomes [1, 0, 1, 1].
 For third query there is no 4th one.
Explanation 2:

 Initially array = [1, 1, 1, 1, 1]. After first query array becomes [1, 1, 0, 1, 1].
 For second query 4th one is at index 5.    
 After third query array remains same [1, 1, 0, 1, 1].
 For fourth query there is no 5th one.'''

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        arr = [1] * A
        T = [0] * (A * 4)

        self.build(0, 0, A - 1, T, arr)

        ans = []
        for i in range(len(B)):
            
            a, b = B[i][0], B[i][1]
            
            if a == 0:
                self.update(0, 0, A-1, b-1, T, arr)
            else:
                if T[0] < b:
                    ans.append(-1)
                else:
                    v = self.query(0, 0, A-1, b, T, arr)
                    ans.append(v)
        
        # for i in range(len(B)):
            
        #     a, b = B[i][0], B[i][1]
            
        #     if a == 0:
        #         self.update(0, 0, A-1, b-1, T, arr)
        #     else:

        #         val_ = -1
        #         st, en = 0, len(arr) - 1

        #         while st <= en:
        #             mid = st + (en - st) // 2

        #             curr = self.range_query(0, 0, len(arr) - 1, 0, mid, T, A)

        #             if curr >= b:
        #                 val_ = mid + 1
        #                 en = mid - 1
                    
        #             else:
        #                 st = mid + 1

        #         ans.append(val_)

        return ans
    
    # Traversing the tree to search for the kth one takes logN time, whereas a binary search approach takes (logN)^2 time (logN for binary search and logN for the range query)

    def build(self, idx, s, e, T, A):

        if s == e:
            T[idx] = A[s]
            return
        
        mid = s + (e - s) // 2

        # Child indices
        l_c = 2 * idx + 1
        r_c = l_c + 1

        # Recursively call to fill left and right indices
        self.build(l_c, s, mid, T, A)
        self.build(r_c, mid + 1, e, T, A)

        # Sum in range
        T[idx] = T[l_c] + T[r_c]
    
    def update(self, idx, s, e, idx_, T, A):

        if s == e:
            T[idx] = 0
            A[idx_] = 0
            return
        
        mid = s + (e - s) // 2

        # Child indices
        l_c = 2 * idx + 1
        r_c = l_c + 1

        if idx_ <= mid:
            # Go to the left subtree
            self.update(l_c, s, mid, idx_, T, A)
        
        else:
            # Go right
            self.update(r_c, mid + 1, e, idx_, T, A)
    
        # Update range sum
        T[idx] = T[l_c] + T[r_c]
    
    def query(self, idx, s, e, k, T, A):

        if s == e:
            return s + 1
        
        mid = s + (e - s) // 2

        # Child indices
        l_c = 2 * idx + 1
        r_c = l_c + 1
        
        if T[l_c] < k:
            # Go right and search K - T[l_c] ones
            return self.query(r_c, mid + 1, e, k - T[l_c], T, A)
        
        else:
            # Go left
            return self.query(l_c, s, mid, k, T, A)
    
    def range_query(self, idx, s, e, L, R, T, A):

        # Three cases, complete overlap, partial overlap or no overlap

        # Complete overlap
        if s >= L and e <= R:
            # Get the value at the index
            return T[idx]
        
        # No overlap
        elif L > e or R < s:
            return 0
        
        # Partial overlap
        else:
            # Check both halfs
            mid = s + (e - s) // 2
            l_c = 2 * idx + 1
            r_c = 2 * idx + 2

            left = self.range_query(l_c, s, mid, L, R, T, A)
            right = self.range_query(r_c, mid + 1, e, L, R, T, A)

        # Return sum of left and right
        return (left + right)