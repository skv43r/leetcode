# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for char_s, char_t in zip(s, t):
            s_dict[char_s] = 1 + s_dict.get(char_s, 0)
            t_dict[char_t] = 1 + t_dict.get(char_t, 0)

        if s_dict == t_dict:
            return True
        else:
            return False

print(Solution().isAnagram('rat', 'car'))