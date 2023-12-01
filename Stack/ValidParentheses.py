#20. Valid Parentheses

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

"""
Time: O(n)
Space: O(n)
"""

class Solution(object):
    def isValid(self, s):
        leftSymbol = []
        for c in s:
            if c in ['(','{','[']:
                leftSymbol.append(c)
            elif c == ')' and len(leftSymbol) != 0 and leftSymbol[-1]=='(':
                leftSymbol.pop()
            elif c == '}' and len(leftSymbol) != 0 and leftSymbol[-1]=='{':
                leftSymbol.pop()
            elif c == ']' and len(leftSymbol) != 0 and leftSymbol[-1]=='[':
                leftSymbol.pop()
            else:
                return False
        return leftSymbol==[]
