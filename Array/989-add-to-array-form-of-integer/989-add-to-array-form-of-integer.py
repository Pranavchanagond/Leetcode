class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=len(num)
        sum=0
        ans=[]
        for i in range(n-1,-1,-1):
                sum=k+num[i]
                ans.append(sum%10)
                k=sum//10
        while k>0:
            ans.append(k%10)
            k=k//10
        ans=ans[::-1]
        return ans