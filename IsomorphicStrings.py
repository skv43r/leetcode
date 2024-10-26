# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s
# can be replaced to get t.
# All occurrences of a character must be replaced with another character while
# preserving the order of characters.
# No two characters may map to the same character,
# but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Explanation:
# The strings s and t can not be made identical as 'o' needs to be mapped
# to both 'a' and 'r'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for char_s, char_t in zip(s, t):
            if char_s in count_s:
                if count_s[char_s] != char_t:
                    return False
            else:
                count_s[char_s] = char_t

            if char_t in count_t:
                if count_t[char_t] != char_s:
                    return False
            else:
                count_t[char_t] = char_s
        
        return True
            
sol = Solution()
print(sol.isIsomorphic("egg", "add"))