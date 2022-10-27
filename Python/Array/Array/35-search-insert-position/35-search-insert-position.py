class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j=0
        i=0
        while(i<len(nums)):
            if(nums[i]<target and nums[i]!=target):
                i+=1
                print(i)
            elif(nums[i]>target):
                #i-=1
                return i
            else:
                return i
        return i    
            
        