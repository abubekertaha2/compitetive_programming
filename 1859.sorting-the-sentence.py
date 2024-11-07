class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        st=sorted(s, key = lambda word: int(word[-1]))
        sent = ' '.join(word[:-1] for word in st)
        return sent
