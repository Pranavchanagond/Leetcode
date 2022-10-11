class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=[]
        l=s.split()
        a=len(l[-1])
        print(len(l[-1]))
        return a