class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        i=0
        ans=0
        for i in range(0,len(nums)):
            c=str(nums[i])
            count=0
            for j in range(0,len(c)):
                    count+=1
            if(count%2==0):
                    ans+=1
        return ans