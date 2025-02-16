# You are given two strings s and t such that every character occurs at most
# once in s and t is a permutation of s.

# The permutation difference between s and t is defined as the sum of the
# absolute difference between the index of the occurrence of each character in s
# and the index of the occurrence of the same character in t.

# Return the permutation difference between s and t.

# Example:
# Input: s = "abcde", t = "edbac"
# Output: 12
# Explanation: The permutation difference between s and t is equal to
# |0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12.

class Solution:
    def findPermutationDifference(s: str, t: str) -> int:
        s_dict = {}
        res = 0
        
        for i in range(len(s)):
            s_dict[s[i]] = i

        for i in range(len(t)):
            res += abs(s_dict[t[i]] - i)

        return res

print(Solution.findPermutationDifference(s = "abcde", t = "edbac"))
