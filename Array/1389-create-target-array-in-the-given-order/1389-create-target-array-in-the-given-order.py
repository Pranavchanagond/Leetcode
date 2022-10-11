class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans=0
        n=len(nums)
        i=j=k=0
        target=[]
        while i<n:
            k=int(nums[i])
            ans=int(index[j])
            target.insert(ans,k)
            i+=1
            j+=1
        return target