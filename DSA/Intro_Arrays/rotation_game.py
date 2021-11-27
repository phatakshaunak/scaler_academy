'''Q5. Rotation Game
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an integer array A and an integer B. You have to print the same array after rotating it B times towards right.

NOTE: You can use extra memory.



Problem Constraints

1 <= |A| <= 106

1 <= A[i] <= 109

1 <= B <= 109



Input Format

First line begins with an integer |A| denoting the length of array, and then |A| integers denote the array elements.
Second line contains a single integer B



Output Format

Print an array of integers which is the Bth right rotation of input array A, on a separate line.



Example Input

Input 1:

 4 1 2 3 4
 2
Input 2:

 3 1 2 2
 3


Example Output

Output 1:

 3 4 1 2
Output 2:

 1 2 2


Example Explanation

Explanation 1:

 [1,2,3,4] => [4,1,2,3] => [3,4,1,2]

Explanation 2:


 [1,2,2] => [2,1,2] => [2,2,1] => [1,2,2]'''

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    def reverse_array(i, j, arr):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1
            j -=1
            
    cases = int(input())
    for i in range(cases):
        arr = [int(i) for i in input().split()]
        
        arr_len = arr[0]
        arr = arr[1:]
        
        # Accounting for rotations exceeding size of the array
        rot = int(input()) % arr_len
        
        reverse_array(0,arr_len-1, arr)
        reverse_array(0, rot-1, arr)
        reverse_array(rot, arr_len-1, arr)
        
        sr = [str(j) for j in arr]
        
        #     #Need to add an extra trailing space after output for solution to be accepted.
        print(' '.join(sr), end=' \n')

    return 0
    
if __name__ == '__main__':
    main()