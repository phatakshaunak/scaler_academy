'''Q4. Word Break II
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given a string A and a dictionary of words B, add spaces in A to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Note : Make sure the strings are sorted in your result.

Input Format:

The first argument is a string, A.
The second argument is an array of strings, B.
Output Format:

Return a vector of strings representing the answer as described in the problem statement.
Constraints:

1 <= len(A) <= 50
1 <= len(B) <= 25
1 <= len(B[i]) <= 20
Examples:

Input 1:
    A = "b"
    B = ["aabbb"]

Output 1:
    []

Input 1:
    A = "catsanddog",
    B = ["cat", "cats", "and", "sand", "dog"]

Output 1:
    ["cat sand dog", "cats and dog"]'''

class Solution:
	# @param A : string
	# @param B : list of strings
	# @return a list of strings
	def wordBreak(self, A, B):

        b_set = set()
        for val in B:
            b_set.add(val)
        
        N, idx, s, cnd, ans = len(A), 0, 0, [], []

        self.backtrack(A, b_set, N, idx, s, cnd, ans)

        return ans

    def backtrack(self, A, b_set, N, idx, s, cnd, ans):

        if idx == N:
            ans.append(' '.join(cnd))
            return
        
        for i in range(idx, N):

            if A[s:i+1] in b_set:
                cnd.append(A[s:i+1])
                self.backtrack(A, b_set, N, i + 1, i + 1, cnd, ans)
                cnd.pop()