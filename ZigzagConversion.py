#6. Zigzag Conversion

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
"""

"""
Time: O(∣s∣)
Space: O(∣s∣)
"""

class Solution(object):
    def convert(self, s, numRows):
        if s is None and numRows <= 0:
            return ""
        if numRows == 1:
            return s
        result =""
        step = 2*numRows-2
        for i in range(0, numRows):
            for j in range(i, len(s), step):
                result += s[j]
                if i!=0 and i!=numRows-1 and (j+step-2*i)<len(s):
                    result += s[j+step-2*i]
        return result