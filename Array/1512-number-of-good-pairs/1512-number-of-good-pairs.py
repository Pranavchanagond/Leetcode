class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(0,len(nums)):
            j=0
            while j<len(nums):
                if nums[i]==nums[j] and i<j:
                    count+=1
                    j+=1
                else:
                    j+=1
        return count