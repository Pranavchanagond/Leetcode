class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums)):
            j=0
            count=0
            while j<len(nums):
                if nums[j]<nums[i] and i!=j:
                    count+=1
                    j+=1
                else:
                    j+=1
            ans.append(count)
        return ans