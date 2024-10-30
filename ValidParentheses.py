# Given a string s containing just the characters '(', ')', '{', '}', '[' , ']',
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {')':  '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in mydict:
                if not stack or stack[-1] != mydict[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack

print(Solution().isValid("({{[{(())]}})}"))