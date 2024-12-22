# You are given a string date representing a Gregorian calendar date in the
# yyyy-mm-dd format.

# date can be written in its binary representation obtained by converting year,
# month, and day to their binary representations without any leading zeroes and
# writing them down in year-month-day format.

# Return the binary representation of date.

# Example 1:
# Input: date = "2080-02-29"
# Output: "100000100000-10-11101"
# Explanation:
# 100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29
# respectively.

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_list = [el for el in date.split('-')]
        s = []
        for el in date_list:
            binary_representation = format(int(el), 'b')
            s.append(binary_representation)
        ans = '-'.join(s)
        return ans
print(Solution().convertDateToBinary(date = "2080-02-29"))