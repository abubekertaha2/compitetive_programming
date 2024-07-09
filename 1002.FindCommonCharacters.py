from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_freq = Counter(words[0])
        for word in words[1:]:
            char_freq &= Counter(word)
        return list(char_freq.elements())
