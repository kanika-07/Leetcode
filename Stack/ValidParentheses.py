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
    """
    isValid that checks whether a given string containing various types of brackets (parentheses, curly braces, and square brackets) has a valid bracket structure. 
    It iterates through the string and uses a stack (implemented with a list) to keep track of the opening brackets encountered. 
    It matches each closing bracket with the corresponding opening bracket popped from the stack. If the brackets match properly and the stack is empty at the end, 
    it returns True; otherwise, it returns False.
    """
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
