'''Q2. Smallest Good Base
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. Now given a string representing A, you should return the smallest good base of A in string format.


Input Format

The only argument given is the string representing A.
Output Format

Return the smallest good base of A in string format.
Constraints

3 <= A <= 10^18
For Example

Input 1:
    A = "13"
Output 1:
    "3"     (13 in base 3 is 111)

Input 2:
    A = "4681"
Output 2:
    "8"     (4681 in base 8 is 11111).'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        
        A = int(A)
        ans = A - 1
        # Iterate over number of 1's
        for i in range(2,65):
            
            s, e = 2, A - 1
            
            while s <= e:
                
                mid = s + (e - s) // 2

                x = A * (mid - 1)
                y = self.power(mid, i + 1) - 1
                
                if y > x: # Reduce base
                    e = mid - 1
                
                elif y < x: # Increase base
                    s = mid + 1
                
                else: # Base found ; update answer and move to a higher i to see if smaller base is possible
                    ans = min(ans, mid)
                    # Break from the while loop as only one base possible for a given value of i
                    break
            
        return ans
    
    def power(self, num, p):
        ans = 1
        while p:
            if p&1:
                ans = ans * num
                num = num * num
            else:
                num = num * num
            p = p // 2
        
        return ans
    
    #Reference: https://www.youtube.com/watch?v=qNDX37Z-fls