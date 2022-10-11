class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=j=0
        while(i < n):
            while(i+1 < n) and (nums[i]==nums[i+1]):
                i+=1
        
            nums[j]=nums[i]
            i+=1
            j+=1
          
        return j
        