# A sentence is a list of words that are separated by a single space with no
# leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i]
# represents a single sentence.

# Return the maximum number of words that appear in a single sentence.


# Example 1:
# Input: sentences = [
#   "alice and bob love leetcode",
#   "i think so too",
#   "this is great thanks very much"
# ]
# Output: 6

from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words = []
        for string in sentences:
            words.append(len(string.split()))
        return max(words)

print(Solution().mostWordsFound(["please wait", "continue to fight", "continue to win"]))
