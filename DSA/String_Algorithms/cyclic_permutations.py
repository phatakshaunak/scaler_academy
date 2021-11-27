'''Q4. Cyclic Permutations
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two binary strings A and B, count how many cyclic permutations of B when taken XOR with A give 0.

NOTE: If there is a string, S0, S1, ... Sn-1 , then it's cyclic permutation is of the form Sk, Sk+1, ... Sn-1, S0, S1, ... Sk-1 where k can be any integer from 0 to N-1.



Problem Constraints

1 ≤ length(A) = length(B) ≤ 105



Input Format

First argument is a string A.
Second argument is a string B.



Output Format

Return an integer denoting the required answer.



Example Input

Input 1:

 A = "1001"
 B = "0011"
Input 2:

 A = "111"
 B = "111"


Example Output

Output 1:

 1
Output 2:

 3


Example Explanation

Explanation 1:

 4 cyclic permutations of B exists: "0011", "0110", "1100", "1001".  
 There is only one cyclic permutation of B i.e. "1001" which has 0 xor with A.
Explanation 2:

 All cyclic permutations of B are same as A and give 0 when taken xor with A. So, the ans is 3.'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        st = B + B
        # Exclude last element to avoid repeating initial pattern
        st = st[:-1]
    
        #Concatenate pattern with delimiter

        conc = A + '$' + st

        # Generate Z array

        Z_array = self.generate_Z(conc)

        # Iterate through Z array and find number of occurences with value == len(A)

        M = len(A)

        ans = 0

        for val in Z_array:
            if val == M:
                ans += 1
        
        return ans

    def generate_Z(self, S):

        N = len(S)
        #Initialize bounding box
        L, R = 0, 0
        Z = [0 for idx in range(N)]

        #Prefix for the first element is simply string length
        Z[0] = N

        #Iterate over remaining elements
        for i in range(1, N):

            # Case when i lies outside bounding box, i.e. i > R
            if i > R:

                #Resize box by moving L and R to i
                L, R = i, i

                #We iterate starting from R to find the prefix value comparing corresponding character in the reference box, This starts from 0, i.e. R = L
                while R < N and S[R] == S[R-L]:
                    #Increment R
                    R += 1
                # Decrement R by 1 as it is one point outside box
                R -= 1
                # Now the elements bounded by L and R represent the prefix for i
                Z[i] = (R - L + 1)
            
            else:
                # Case when i lies within the bounding box

                #Subcase includes a condition when the value of the prefix for the corresponding reference box is within the reference box
                # The corresponding pointer now can lie at i - L
                j = i - L

                # Check if prefix at j is less than elements between j and R
                if Z[j] < (R - i + 1):
                    #Simply copy j's value into i
                    Z[i] = Z[j]
                else:
                    # Subcase when the values lie at the boundary of reference box or out of it. We can be sure that the ans at i is atleast the same as values R - i + 1
                    #We can simply resize by moving L to i
                    L = i

                    # Then simply iterate from R until there is no match. This is similar to the previous case when i > R

                    #We iterate starting from R to find the prefix value comparing corresponding character in the reference box, This starts from 0, i.e. R = L
                    while R < N and S[R] == S[R-L]:
                        #Increment R
                        R += 1
                    # Decrement R by 1 as it is one point outside box
                    R -= 1
                    # Now the elements bounded by L and R represent the prefix for i
                    Z[i] = (R - L + 1)
        
        return Z