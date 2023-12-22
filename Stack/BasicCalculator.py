# 224. Basic Calculator
"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""
"""
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def calculate(self, s):
        ans = 0
        num = 0
        sign = 1
        stack = [sign]  # stack[-1]: the current environment's sign
        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c == '+' or c == '-':
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0
        return ans + sign * num
"""
Sample
Input
s = "1 + 1"
Output
2
Expected
2
"""
