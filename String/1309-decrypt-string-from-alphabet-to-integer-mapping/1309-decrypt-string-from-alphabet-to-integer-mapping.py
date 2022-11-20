class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=""
        n=len(s)
        i=n-1
        while (i > -1):
            if(s[i]!="#"):
                ans+=chr(int(s[i])+96)
                i-=1
            else:
                ans+=chr((int((s[i-2])+(s[i-1])))+96)
                i-=3
        return ans[::-1]