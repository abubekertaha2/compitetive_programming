class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=""
        indx=0
        while indx <len(s):
            if( indx + 2) <len(s) and s[indx+2]=='#':
                val=int(s[indx:indx+2])
                ans+=chr(96 + val)
                indx+=3
            else:
                val=int(s[indx])
                ans+=chr(96+val)
                indx+=1
        return ans
      
