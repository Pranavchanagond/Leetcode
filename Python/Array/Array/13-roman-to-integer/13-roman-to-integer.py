class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        i=n-1
        o=0
        
        p={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        while i >= 0:
            if i<n-1 and p[s[i]] < p[s[i+1]]:
                o=o-p[s[i]]
             #   i=i-1
            else:
                o=o+p[s[i]]
            i=i-1
        
        return o
        
        