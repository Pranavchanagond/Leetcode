class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        ob=["{","(","["]
        cb=["}","]",")"]
        d={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        i=0
        if(s[0] in cb or s[-1] in ob):
            return False
    
        while(i<len(s)):
            if(s[i] in ob):
                res.append(s[i])
            else:
                n=d[s[i]]
                if(len(res)>0 and res[-1]==n):
                    res.pop()
                else:
                    return False
       
            i+=1                
        if(len(res)==0):
             return True
        else:
             return False
        