'''Q4. Maximum Frequency stack
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given a matrix A which represent operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it.

Operations are of two types:

1 x: push an integer x onto the stack and return -1

2 0: remove and return the most frequent element in the stack.

If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.

A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed.



Problem Constraints

1 <= N <= 100000

1 <= A[i][0] <= 2

0 <= A[i][1] <= 109



Input Format

The only argument given is the integer array A.



Output Format

Return the array of integers denoting answer to each operation.



Example Input

Input 1:

A = [
            [1, 5]
            [1, 7]
            [1, 5]
            [1, 7]
            [1, 4]
            [1, 5]
            [2, 0]
            [2, 0]
            [2, 0]
            [2, 0]  ]
Input 2:

 A =  [   
        [1, 5]
        [2 0]
        [1 4]   ]


Example Output

Output 1:

 [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]
Output 2:

 [-1, 5, -1]


Example Explanation

Explanation 1:

 Just simulate given operations
Explanation 2:

 Just simulate given operations'''

 class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):

        hm, st_hm = {}, {}
        max_freq = 0
        ans = []

        for op in A:
            t = op[0]
            val = op[1]
            # Push
            if t == 1:

                # Update with -1 for push operation
                ans.append(-1)
                
                if val not in hm:
                    hm[val] = 1
                else:
                    hm[val] += 1
                
                # Storing frequency stacks
                freq = hm[val]
                
                if freq not in st_hm:
                    st_hm[freq] = [val]
                    
                    # Update maximum frequency
                    max_freq = max(max_freq, freq)
                
                else:
                    st_hm[freq].append(val)
                    # Update maximum frequency
                    max_freq = max(max_freq, freq)
            
            # Pop
            else:
                
                if st_hm[max_freq]:
                    ans.append(st_hm[max_freq][-1])
                    hm[st_hm[max_freq][-1]] -= 1

                    st_hm[max_freq].pop()

                    if not st_hm[max_freq]:
                        max_freq -= 1
                
                # else:
                #     max_freq -= 1

                # if not st_hm[max_freq]:
                #     del st_hm[max_freq]
                #     max_freq -= 1
                    
        return ans
