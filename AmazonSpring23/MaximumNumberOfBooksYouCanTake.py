# 2355. Maximum Number of Books You Can Take
"""
You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on the ith shelf of a bookshelf.
You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n. For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.
Return the maximum number of books you can take from the bookshelf.
"""
"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        # dp[i] := the maximum the number of books we can take from books[0..i] with taking all of
        # books[i]
        dp = [0] * len(books)
        stack = [] # the possible indices we can reach

        for i, book in enumerate(books):
            # we may take all of books[j], where books[j] < books[i] - (i-j).
            while stack and books[stack[-1]] >= book - (i-stack[-1]):
                stack.pop()
            # We can now take books[j+1..i]
            j = stack[-1] if stack else -1
            lastPicked = book - (i-j)+1
            if lastPicked > 1:
                # book + (book - 1)+ ... + (book-(i-j)+1)
                dp[i] = (book + lastPicked) * (i-j)//2
            else:
                # 1 + 2 + ... + book
                dp[i] = book * (book+1)//2
            if j>= 0:
                dp[i] += dp[j]
            stack.append(i)
        return max(dp)
"""
Input
books = [8,5,2,7,9]
Output
19
"""
