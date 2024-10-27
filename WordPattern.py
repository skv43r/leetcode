# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between
# a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        dict_p = {}
        dict_s = {}
        for char_p, char_s in zip(pattern, s.split()):
            if char_p in dict_p:
                if dict_p[char_p] != char_s:
                    return False
            else:
                dict_p[char_p] = char_s

            if char_s in dict_s:
                if dict_s[char_s] != char_p:
                    return False
            else:
                dict_s[char_s] = char_p
        
        return True
    
print(Solution().wordPattern("aaa", "aa aa aa aa"))