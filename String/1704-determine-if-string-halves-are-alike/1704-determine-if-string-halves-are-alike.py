class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)//2
        a=b=""
        count1=count2=0
        for i in range(0,n):
            a+=s[i]

        for i in range(n,len(s)):
            b+=s[i]

        for i in range(0,len(a)):
            if(a[i]=='a' or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or
                a[i]=='A' or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U" ):
                count1+=1

        for i in range(0,len(b)):
            if(b[i]=='a' or b[i]=="e" or b[i]=="i" or b[i]=="o" or b[i]=="u" or
                b[i]=='A' or b[i]=="E" or b[i]=="I" or b[i]=="O" or b[i]=="U" ):
                count2+=1

        if count1==count2:
            return True
        else:
            return False