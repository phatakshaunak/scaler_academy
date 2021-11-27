'''Q1. NESTED_CMPL2
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
What is the time complexity of the following code :

    int a = 0;
    for (i = 0; i < N; i++) {
        for (j = N; j > i; j--) {
            a = a + i + j;
        }
    }'''

# TC: O(N^2)

'''Q2. NESTED_CMPL3
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
What is time complexity of following code :

        int count = 0;
        for (int i = N; i > 0; i /= 2) {
            for (int j = 0; j < i; j++) {
                count += 1;
            }
        }'''

# TC: O(N)

'''Q3. WHILE_CMPL
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
What is the time complexity of the following code :

        int a = 0, i = N;
        while (i > 0) {
            a += i;
            i /= 2;
        }'''

# TC: O(log(N))

'''Q1. CHOOSE2
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Which of the given options provides the increasing order of complexity of functions f1, f2, f3 and f4:

f1(n) = 2^n

f2(n) = n^(3/2)

f3(n) = nLogn

f4(n) = n^(Logn)

Choose the correct answer from below:
f2, f3, f4, f1
f2, f3, f1, f4
correct answer: f3, f2, f4, f1
f3, f2, f1, f4
'''

'''Q2. CHOOSE3
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
In a competition, four different functions are observed. All the functions use a single for loop and within the for loop, same set of statements are executed.

Consider the following for loops:

  A) for(i = 0; i < n; i++)

  B) for(i = 0; i < n; i += 2)

  C) for(i = 1; i < n; i *= 2)

  D) for(i = n; i > -1; i /= 2)
  
  Choose the correct answer from below:
B
A
D
C (correct answer)
  '''

'''Q3. AMORTIZED1
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
What is the time complexity of the following code :

        int j = 0;
        for(int i = 0; i < n; ++i) {
            while(j < n && arr[i] < arr[j]) {
                j++;
            }
        }

Choose the correct answer from below:
O(n(logn)^2)
Correct answer: O(n)
O(n^2)
O(nlogn)
Can't say. Depends on the value of arr.
Submit
        '''

