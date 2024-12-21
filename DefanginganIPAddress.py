# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        mylist = address.split('.')
        s = '[.]'.join(mylist)
        return s

print(Solution().defangIPaddr("255.100.50.0"))