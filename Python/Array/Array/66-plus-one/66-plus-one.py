class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=0
        k=0
        n=len(digits)
        while(i<n):
            if(i < n):
                k=k+(digits[i]*pow(10,(n-1-i)))
                i+=1
        
        k+=1
        p=str(k)
        v=list(p)
        return v